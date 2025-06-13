import csv
from datetime import datetime
import pytz

log_range = '1630-1705'
input_file = '{}.csv'.format(log_range)
output_file = 'parsed-{}.csv'.format(log_range)

# output fields
fieldnames = [
    'timestamp', 'version', 'account_id', 'interface_id',
    'srcaddr', 'dstaddr', 'srcport', 'dstport',
    'protocol', 'packets', 'bytes', 'start',
    'end', 'action', 'log_status'
]

# UNIX epoch time → human readable time (LA timezone)
def to_readable_time(epoch_seconds):
    la_tz = pytz.timezone('America/Los_Angeles')
    dt_utc = datetime.fromtimestamp(int(epoch_seconds), tz=pytz.utc)
    dt_local = dt_utc.astimezone(la_tz)
    return dt_local.strftime('%Y-%m-%d %H:%M:%S')

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        timestamp_ms = int(row['timestamp'])
        message_parts = row['message'].split()

        if len(message_parts) == 14:
            start_epoch = message_parts[10]
            end_epoch = message_parts[11]

            new_row = {
                'timestamp': to_readable_time(timestamp_ms / 1000),
                'version': message_parts[0],
                'account_id': message_parts[1],
                'interface_id': message_parts[2],
                'srcaddr': message_parts[3],
                'dstaddr': message_parts[4],
                'srcport': message_parts[5],
                'dstport': message_parts[6],
                'protocol': message_parts[7],
                'packets': message_parts[8],
                'bytes': message_parts[9],
                'start': to_readable_time(start_epoch),
                'end': to_readable_time(end_epoch),
                'action': message_parts[12],
                'log_status': message_parts[13]
            }
            writer.writerow(new_row)
        else:
            print(f"[Warning] Message field does not incloud 14 fields: {row['message']}")
