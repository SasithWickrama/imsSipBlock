from jnius import autoclass


BufferedReader = autoclass('java.io.BufferedReader')
InputStreamReader = autoclass('java.io.InputStreamReader')
PrintWriter = autoclass('java.io.PrintWriter')
Socket = autoclass('java.net.*')


socket = Socket("10.68.131.71", 31114)
inval = BufferedReader(InputStreamReader(socket.getInputStream()))
out = PrintWriter(socket.getOutputStream(), True)

out.println("LGI:OP=\"NBI_MML_Test_User\", PWD=\"Test@123\";")
print(inval)