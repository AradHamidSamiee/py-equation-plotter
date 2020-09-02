import matplotlib.pyplot as plt

vertices = list()

# ---------- private use function ---------- FIBONACCI
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def list_fibonacci(n):
    vertices.clear()
    m = n
    for i in range(int(m)):
        x = fibonacci(i + 1)
        vertices.append(x)
        print(i + 1, ':', x)
# ---------------------- END -------------------------

# ---------- private use function ---------- FIBONACCI


# ---------- global use function ----------- PLOT
def plot_line():
    plt.plot(vertices)
    plt.ylabel('?')
    plt.show()

def plot_vertex():
    plt.plot(vertices, 'ro') # 'ro' = red circles - 'g^' = green triangles - 'b--' = blue dashes
    plt.axis([-0.9, int(vertices[len(vertices)-1]) , -0.9, int(vertices[len(vertices)-1])]) # first num: axis y min, second: axis y max, third: axis x min
    plt.ylabel('?')
    plt.show()
# ---------------------- END -------------------------

# ---------- global use function -------------- IMPORT
def import_file():
    file = input('  file name: ')
    imported_file = open(file)
    vertices.clear()
    for line in imported_file:
        print(line.replace(' ',''))
        vertices.append(line.replace(' ',''))
# ---------------------- END -------------------------

# ---------- global use function ---------- help
def help():
    help_file = open('help.ahs')
    for line in help_file:
        print(line,end='')
# ---------------------- END -------------------------

# ---------------------- MAIN ------------------------
print('- you can ask for help by typing help -')
while True:
    command = input('> ')
    if command.replace(' ','') == 'end':
        quit()
    elif command.replace(' ','') == 'help':
        help()
    elif command.replace(' ','') == 'fib':
        n = input('  fib(n) - n:')
        list_fibonacci(n)
        print('listed!')
    elif command.replace(' ','') == 'import':
	    import_file()
    elif command.lower().replace(' ','') == 'plotline':
        plot_line()
    elif command.lower().replace(' ','') == 'plotvertex':
        plot_vertex()
# ---------------------- END -------------------------
