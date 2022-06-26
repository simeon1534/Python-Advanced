with open('text.txt', 'r') as text_fh_r:
    counter = 0
    marks = ["-", ",", ".", "!", "?"]
    for line in text_fh_r:
        if counter==0 or counter % 2 == 0 :
            new_line=line
            for mark in marks:
                new_line=new_line.replace(mark,'@')
            new_line=new_line.split()
            new_line=new_line[::-1]
            with open('output.txt', 'a') as text_fh_w:
                print(f"{' '.join(new_line)}", file=text_fh_w)
        counter += 1
