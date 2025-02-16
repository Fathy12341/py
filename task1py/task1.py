def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_number(num):
    result = []
    
    if num % 2 == 0:
        result.append("زوجي")
    else:
        result.append("فردي")
    
    if is_prime(num):
        result.append("أولي")
    
    return result

# طلب إدخال الرقم من المستخدم
num = int(input("أدخل الرقم: "))

# تحديد خصائص الرقم
result = check_number(num)

# عرض النتيجة
if len(result) == 0:
    print("الرقم ليس زوجيًا ولا فرديًا ولا أوليًا.")
else:
    print(f"الرقم {num} هو: {', '.join(result)}")