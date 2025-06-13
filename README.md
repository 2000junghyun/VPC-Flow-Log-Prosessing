# VPC-Flow-Log-Prosessing
## Problem

- The log file contains only two fields: `timestamp` and `message`, which makes analysis difficult.
- The default time format is in UNIX epoch time, making it hard to interpret.

## Solution

- Refined the log fields for better structure and clarity:
    
    ```python
    python
    CopyEdit
    fieldnames = [
        'timestamp', 'version', 'account_id', 'interface_id',
        'srcaddr', 'dstaddr', 'srcport', 'dstport',
        'protocol', 'packets', 'bytes', 'start',
        'end', 'action', 'log_status'
    ]
    
    ```
    
- Converted UNIX epoch time to human-readable time in LA timezone.
- Designed the script so input and output file names can be easily customized.

## 결과

### Before

![image.png](attachment:a541035a-6c01-4311-91f4-efa067809f3f:image.png)

### After

## Expected Benefits

- Enables generation of a structured base file for more precise log filtering.
- Makes timestamps easier to interpret by using a more readable time format.
