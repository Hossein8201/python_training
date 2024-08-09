string_in = input()
string_part = ''
string_out = input()
index_begin = 0
remain = 0
for i in range(len(string_in)):
    if(len(string_out) > len(string_in)):
        string_part = string_in[i:len(string_in)] + string_in[0:i]
        if string_part == string_out[0:len(string_in)]:
            index_begin = len(string_out) // len(string_in)
            string_part *= index_begin
            remain = len(string_out) % len(string_in)
            if(remain >= len(string_in) - i):
                string_part += string_in[i:len(string_in)] 
                remain -= (len(string_in) - i)
                string_part += string_in[0:remain]
            else:
                string_part += string_in[i:remain+i]
            # print(string_part)
            if(string_part == string_out):
                print("Yes")
                exit()
    else:
        if(string_in in string_out):
            print("Yes")
            exit()

print("No")