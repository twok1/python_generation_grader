def log_for(logfile, date_str):
    with open(logfile, 'r', encoding='utf-8') as rf, open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as wf:
        for line in rf.readlines():
            date, *str = line.split()
            if date == date_str:
                wf.write(' '.join(str) + '\n')