class StackLang:
    def __init__(self):
        self.stack = []
        self.labels = {}
        self.pc = 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def add(self):
        b = self.pop()
        a = self.pop()
        if a is not None and b is not None:
            self.push(a + b)

    def sub(self):
        b = self.pop()
        a = self.pop()
        if a is not None and b is not None:
            self.push(a - b)

    def mul(self):
        b = self.pop()
        a = self.pop()
        if a is not None and b is not None:
            self.push(a * b)

    def div(self):
        b = self.pop()
        a = self.pop()
        if a is not None and b is not None and b != 0:
            self.push(a // b)

    def mod(self):
        b = self.pop()
        a = self.pop()
        if a is not None and b is not None and b != 0:
            self.push(a % b)

    def bitwise_and(self):
        b = self.pop()
        a = self.pop()
        if a is not None and b is not None:
            self.push(a & b)

    def bitwise_or(self):
        b = self.pop()
        a = self.pop()
        if a is not None and b is not None:
            self.push(a | b)

    def bitwise_xor(self):
        b = self.pop()
        a = self.pop()
        if a is not None and b is not None:
            self.push(a ^ b)

    def print_stack(self):
        print(self.pop())

    def print_char(self):
        char_value = self.pop()
        if char_value is not None:
            print(chr(char_value), end='', flush=True)

    def negative(self):
        value = self.pop()
        if value is not None:
            self.push(0 if value < 0 else value)

    def input_chars(self):
        user_input = input()
        for char in user_input:
            self.push(ord(char))
    def leng(self):
        self.stack.append(len(self.stack)+1)
    def execute(self, code):
        code_lines = code.splitlines()
        self.labels = {line.split(':')[0].strip(): idx for idx, line in enumerate(code_lines) if ':' in line}
        
        while self.pc < len(code_lines):
            line = code_lines[self.pc].strip()
            if line.startswith("push"):
                _, value = line.split()
                if value.startswith('"') and value.endswith('"'):
                    for char in value[1:-1]:
                        self.push(ord(char))
                elif value.startswith("'") and value.endswith("'"):
                    self.push(ord(value[1]))
                else:
                    self.push(int(value))
            elif line == '+':
                self.add()
            elif line == '-':
                self.sub()
            elif line == '*':
                self.mul()
            elif line == '/':
                self.div()
            elif line == '%':
                self.mod()
            elif line == '&':
                self.bitwise_and()
            elif line == '|':
                self.bitwise_or()
            elif line == '^':
                self.bitwise_xor()
            elif line == 'print':
                self.print_stack()
            elif line == 'printc':
                self.print_char()
            elif line == 'len':
                self.leng()    
            elif line == 'pop': self.pop()                            
            elif line == 'negative':
                self.negative()
            elif line == 'input':
                self.input_chars()
            elif line.startswith('if'):
                condition, label = line[3:].split()
                result = self.pop()
                self.push(result)
                if str(result) == condition:
                    self.pc = self.labels[label]
            elif line.startswith('goto'):
                label = line[5:].strip()
                self.pc = self.labels[label]
            elif line == 'dupe':
                a = self.stack.pop()
                self.stack.append(a)
                self.stack.append(a)
            elif line == 'die':
                break
            self.pc += 1


lang = StackLang()
code = """
push "!dlrow"
push 32 
push "olleh"
start:
len
if 1 end
pop 
printc
goto start
end:
die
"""
lang.execute(code)
