from termcolor import colored
def printMT(state, head, tape):
    print(f"\tstate: {state},\thead pos: {head},\t tape: ", end="")
        
    for i in range(len(tape)):
                    if (i == head):
                            print(colored(f"{tape[i]}", "green"), end=' ')
                    else:
                            print(tape[i], end=' ')
    print()

class TuringMachineMulti:
    def __init__(self, tape):
        self.tape = list(tape)  # Лента
        self.head = 0            # Позиция головки
        self.state = 'start'     # Начальное состояние
    def step(self):
        if self.state == 'start':
            while self.head < len(self.tape):
                printMT(self.state, self.head, self.tape)
                self.head += 1
            self.tape.append(' ')
            self.head += 1

            self.state = 'multi_in_start'    
            printMT(self.state, self.head, self.tape)
        elif self.state == 'multi_in_start':
            while self.head != 0 and self.tape[self.head-1] != '_':
                self.head-=1
                printMT(self.state, self.head, self.tape)
            if (self.tape[self.head] == '*'):
                self.state='delete_1_for_second_muliplayer'
            else:
                self.state = 'multi_first_multiplayer'
        elif self.state == 'multi_first_multiplayer':
            n = len(self.tape)
            while (self.head < n):
                self.head+=1
                if (self.state == 'multi_first_multiplayer' and self.tape[self.head] != '*'):
                    self.tape.append('1')
                if (self.tape[self.head - 1] == '*'):
                    self.tape[self.head] = '_'
                    self.state = 'multi_first_multiplayer_done'
                printMT(self.state, self.head, self.tape)
            self.state = 'delete_1_for_second_muliplayer'
            self.head+=1
            printMT(self.state, self.head, self.tape)
        elif self.state == 'delete_1_for_second_muliplayer':
            self.head = 0
            printMT(self.state, self.head, self.tape)
            while self.tape[self.head] != '*':
                self.head += 1
                printMT(self.state, self.head, self.tape)
            self.head += 1
            printMT(self.state, self.head, self.tape)
            while self.tape[self.head] != ' ' and self.tape[self.head] != '1':
                self.head += 1
                printMT(self.state, self.head, self.tape)
            if (self.tape[self.head] == ' '):
                self.state = 'end_multi'
            else:
                self.tape[self.head] = '_'
                self.state='create_tape_for_add'
        elif self.state == 'create_tape_for_add':
            self.head = 0
            printMT(self.state, self.head, self.tape)
            self.tape.append('+')
            printMT(self.state, self.head, self.tape)
            while self.tape[self.head] != '*':
                self.tape.append('1')
                self.head+=1
                printMT(self.state, self.head, self.tape)
            self.state='start_add_prepare'
            printMT(self.state, self.head, self.tape)
        elif self.state == 'start_add_prepare':
            self.head = 0
            printMT(self.state, self.head, self.tape)
            while self.tape[self.head] != ' ':
                self.head +=1
                printMT(self.state, self.head, self.tape)
            self.state = 'start_add'
        elif self.state == 'start_add':
            # Ищем символ '+'
            while self.tape[self.head] != '+':
                printMT(self.state, self.head, self.tape)
                self.head += 1
            self.head += 1  # Пропускаем '+'
            self.state = 'add'
            printMT(self.state, self.head, self.tape)
        elif self.state == 'add':
            while self.head < len(self.tape):
                self.tape[self.head - 1] = self.tape[self.head]
                self.head += 1
                printMT(self.state, self.head, self.tape)
            self.state = 'end_add'
            del self.tape[len(self.tape) - 1]
            self.head -= 1
            printMT(self.state, self.head, self.tape)
        elif self.state == 'end_add':
            self.head = 0
            self.state= 'delete_1_for_second_muliplayer'
            printMT(self.state, self.head, self.tape)
        elif self.state == 'end_multi':
            self.head = 0
            printMT(self.state, self.head, self.tape)
            while (self.tape[self.head] != ' '):
                del self.tape[self.head]
                printMT(self.state, self.head, self.tape)
            self.state = 'halt'
            printMT(self.state, self.head, self.tape)
    def run(self):
        while self.state != 'halt':
            self.step()
        return ''.join(map(str, self.tape))
# Пример использования
input_data = "11111111111*111111111"
tm = TuringMachineMulti(input_data)
result = tm.run()
print(f"Результат умножения: {result}")  