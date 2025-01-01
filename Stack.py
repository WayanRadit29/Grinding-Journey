stack = list(map(int, input().split(',')))

def push(stack, N):
    return stack.append(N)

def pop(stack):
    if len(stack) < 0:
        return "Stack Kosong"
    else:
        return stack.pop()

def peek(stack):
    if len(stack) < 0:
        return "Stack Kosong"
    else:
        return stack[-1]

def isEmpty(stack):
    return len(stack) == 0

push(stack, 15)
print(f"Stack ditumpuk dengan angka baru yaitu 15, hasilnya : {stack}")
pop(stack)
print(f"Stack setelah angka paling atas diambil : {stack}")
pop(stack)
print(f"Stack setelah angka paling atas diambil lagi : {stack}")
print(f"Angka yang berada di paling atas stack : {peek(stack)}")
print(f"Mengecek apakah stack kosong : {isEmpty(stack)}")

