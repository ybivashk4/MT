from termcolor import colored
def printMT(state, head, tape):
    print(f"state: {state},\thead pos: {head},\t tape: ", end="")
        
    for i in range(len(tape)):
                    if (i == head):
                            print(colored(f"{tape[i]}", "green"), end=' ')
                    else:
                            print(tape[i], end=' ')
    print()
class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  # Лента
        self.head = 0            # Позиция головки
        self.state = 'start'     # Начальное состояние
    def step(self):
        if self.state == 'start':
            # ставим ' ' в конец
            while self.head < len(self.tape):
                printMT(self.state, self.head, self.tape)
                self.head += 1
            self.tape.append(" ")
            self.head = 0
            printMT(self.state, self.head, self.tape)
            self.state = "after_setup"
        elif self.state == "after_setup":
            while self.tape[self.head] != '+':
                printMT(self.state, self.head, self.tape)
                self.head += 1
            printMT(self.state, self.head, self.tape)
            self.state = "start_add"
            self.head += 1
        elif self.state == 'start_add':
            carry = 0
            i = self.head - 2
            while self.tape[self.head] != ' ':
                self.head+=1
                printMT(self.state, self.head, self.tape)
            self.state = 'add'
            self.head-=1
            while (self.state != "end_add"):
                printMT(self.state, self.head, self.tape)
                if (self.state == 'add'):
                    # print(f"debuf data: \n {carry}, {self.tape[self.head]}, {int(self.tape[self.head])}, {carry}, {int(self.tape[i])}")
                    temp_carry = (int(self.tape[self.head]) + carry + int(self.tape[i])) >= 2
                    self.tape[self.head] = (int(self.tape[self.head]) + carry + int(self.tape[i])) % 2
                    carry = temp_carry
                elif (self.state == 'add_without_right'):
                    temp_carry = (0 + carry + int(self.tape[i])) >= 2
                    self.tape[self.head] = (0 + carry + int(self.tape[i])) % 2
                    carry = temp_carry
                elif (self.state == 'add_without_left'):
                    temp_carry = (int(self.tape[self.head]) + carry + 0) >= 2
                    self.tape[self.head] = (int(self.tape[self.head]) + carry + 0) % 2
                    carry = temp_carry
                i -= 1
                self.head -= 1
                if ( (self.state == 'add_without_right' or self.tape[self.head] == '+') and i < 0):
                    self.state = 'end_add'
                elif (self.tape[self.head] == '+'):
                    self.state = 'add_without_right'
                elif (i < 0):
                    self.state = 'add_without_left'
            
            while (self.head != 0):
                printMT(self.state, self.head, self.tape)
                self.tape[self.head] = ''
                self.head -= 1
            self.state = 'halt'
    def run(self):
        while self.state != 'halt':
            self.step()
        return ''.join(map(str, self.tape))

# Пример использования
input_data = input()  # 63 + 15 
tm = TuringMachine(input_data)
result = tm.run()
print(f"Результат сложения: {result}")  
# print(int('101110', 2), bin(78))