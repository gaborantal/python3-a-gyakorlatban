
msg = "Ez,egy,szoveg;ez, akarjuk, szetdarabolni"
print(msg.split(","))
print(msg.split(",")[0])
print(msg.split(",")[1:])
print(msg.split(",")[1:3])
print(msg.split(",")[:-1])
print(msg.split(",")[1:-2])
print("--------------------------")
print("@".join(msg.split(",")[1:]))
print("--------------------------")
print(msg.split(",", 2)[0])
print(msg.split(",", 2)[1])
print(msg.split(",", 2)[2])
