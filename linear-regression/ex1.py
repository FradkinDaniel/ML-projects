def load_data():
    matrixD = []
    matrixY = []
    f = open(filename, 'r')

    while True:
        line = f.readline()
        line = line.rstrip('\n')
        if len(line) == 0:
            break

        columns = line.strip().split('  ')
        last_column = columns.pop()
        matrixD.append([float(col) for col in columns])
        matrixY.append([float(last_column)])

    return [matrixD,matrixY]


def gradientDescent(filename, alpha=1.4, max_iter=1000, threshold=0.001):
    cost_J = float('inf')
    iter = 1
    Costs = []
    Data, Y = load_data(filename)
    # display_graph(Data, Y, 0)
    # display_graph(Data, Y, 1)
    Data = scale(Data, 0)
    Data = select_single(Data, 0)
    Hypothesis = [0.0, 0.0]

    while(True):
        error = computeErrors(Data, Y, Hypothesis)
        cost = computeCost(Data,Y,Hypothesis)
        grandiant = computeGradient(Data,error)

        if(cost_J<cost):
            print("Gradient descent terminating after %d iterations, new cost is higher(%f) from previous cost(%f)"% (iter + 1, cost, cost_J))
            break

        Costs.append(cost)
        Hypothesis = updateHypothsis(Hypothesis, alpha, grandiant)
        cost_J = cost

        if (iter > max_iter):
            print("Gradient descent terminating after %d iterations (max_iter)"% (iter + 1))
            break

        if len(Costs) > 1 and abs(Costs[-1] - Costs[-2]) < threshold:
            print("Gradient descent terminating after %d iterations.Improvement was: %f – below threshold (%f)"% (iter + 1, abs(Costs[-1] - Costs[-2]), threshold))
            break

        iter+=1
    print(cost_J)
    return Costs, Hypothesis

def display_graph(Data:list, Y:list, feature):
    data_values = [row[feature] for row in Data]
    y_values = [row[0] for row in Y]
    plt.plot(data_values, y_values, 'o')  # 'o' for scatter plot
    if feature == 0:
        plt.title("New cost vs second hand cost")
        plt.xlabel("New cost")
        plt.ylabel("Second hand cost")
    else:
        plt.title("Phone age vs second hand cost")
        plt.xlabel("Phone age")
        plt.ylabel("Second hand cost")
    plt.grid(True)
    plt.show()

def scale(mat: list, col):
    max = mat[0][col]

    for i in mat:
        if i[col] > max:
            max = i[col]

    for i in mat:
        i[col] = i[col] / max
    return mat

def predict_value(Example: list, Hypothesis: list):
    prediction = 0
    for i in range(Example.__len__()):
        prediction += Example[i] * Hypothesis[i]
    return prediction


def select_single(D,n):
    D1 = []
    for i in range (D.__len__()):
        D1.append(D[i][n])
    return addOnesColum(D1)

def addOnesColum(D1: list):
    for i in range(D1.__len__()):
        D1[i] = [1, D1[i]]
    return D1

def computeErrors (Data: list, Y:list, Hypothesis:list):
    v = []
    if(Data.__len__()!= Y.__len__()):
        return []
    for i in range(0, Data.__len__()):
        v.append(predict_value(Data[i], Hypothesis) - Y[i][0])
    return v
def computeCost(Data:list , Y:list , Hypothesis:list):
    errors = 0
    v:list = computeErrors(Data,Y,Hypothesis)
    for i in range(0, (v.__len__())):
        errors += v[i]*v[i]
    return errors/(2*Data.__len__())
def computeGradient(Data:list, Errors:list):
    gradiants = []
    g =0
    print(Data.__len__() == Errors.__len__())
    for i in range(0,Data[0].__len__()):
        for j in range(0,Data.__len__()):
            g += Data[j][i]*Errors[j]
        g /= Data.__len__()
        gradiants.append(g)
    return gradiants

def updateHypothsis(Hypothesis, alpha, Gradient):
    new = [Hypothesis[i] - alpha*Gradient[i] for i in range(0,Hypothesis.__len__())]
    return new

if __name__ == '__main__':
    costs, hypothesis = gradientDescent("smartphone.txt", 1.4)
    plt.plot(costs)
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Cost vs Iterations')
    plt.show()