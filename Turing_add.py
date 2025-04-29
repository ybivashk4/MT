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
            self.state = 'halt'
            self.tape[len(self.tape) - 1] = ' '
            printMT(self.state, self.head, self.tape)

    def run(self):
        while self.state != 'halt':
            self.step()
        return ''.join(map(str, self.tape))

# Пример использования
input_data = "111111+1111"
tm = TuringMachine(input_data)
result = tm.run()
print(f"Результат сложения: {result}")  
# print(int('101110', 2), bin(78))
