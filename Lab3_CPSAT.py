from ortools.sat.python import cp_model

def solve_optimization_problem():

    model = cp_model.CpModel()


    var_upper_bound = 20

    # Змінні X1, X2, ..., X6
    X1 = model.NewIntVar(0, 20, 'X1')
    X2 = model.NewIntVar(0, 20, 'X2')
    X3 = model.NewIntVar(0, 0, 'X3')
    X4 = model.NewIntVar(0, 0, 'X4')
    X5 = model.NewIntVar(0, 0, 'X5')
    X6 = model.NewIntVar(0, 0, 'X6')


    model.Add(15 * X1 + 20 * X2 - 10 * X4 <= 120)
    model.Add(X1 + 2 * X2 - X3 <= 8)
    model.Add(4 * X1 - X5 <= 16)
    model.Add(4 * X2 - X6 <= 12)


    model.Minimize(-2 * X1 - 2 * X2)


    solver = cp_model.CpSolver()
    status = solver.Solve(model)


    if status == cp_model.OPTIMAL:
        print('Optimal solution found:')
        print(f'X1 = {solver.Value(X1)}')
        print(f'X2 = {solver.Value(X2)}')
        print(f'X3 = {solver.Value(X3)}')
        print(f'X4 = {solver.Value(X4)}')
        print(f'X5 = {solver.Value(X5)}')
        print(f'X6 = {solver.Value(X6)}')
        print('Objective function Q =', -2 * solver.Value(X1) - 2 * solver.Value(X2))
    else:
        print('No optimal solution found.')


solve_optimization_problem()
