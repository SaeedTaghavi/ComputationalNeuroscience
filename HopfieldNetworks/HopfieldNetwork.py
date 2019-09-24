#for the submission uncomment the submission statements
#so submission.README

from math import *

from submission import *

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False
    

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")
    
    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "
        
        if d3:
            word+="_"
        else:
            word+=" "
        
        if d2:
            word+="|"
        else:
            word+=" "
        
        print(word)

    

    pattern_b=list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))
    
    
def weight_matrix(p1, p2, p3):
    matrix = [[0]*11 for i in range(0,11)]
    for i in range(0,11):
        for j in range(0,11):
            if i != j:
                matrix[i][j] = 1/3 * (p1[i]*p1[j] + p2[i]*p2[j] + p3[i]*p3[j])
    return matrix
    

def evolve_network(pattern, weights):
    new_pattern = [0]*11
    for i in range(0, 11):
        total = 0
        for j in range(0, 11):
            if i != j:
                total += (weights[i][j] * pattern[j])
        if total > 0:
            new_pattern[i] = 1
        else:
            new_pattern[i] = -1
    return new_pattern


def compare_patterns(p1, p2):
    for i in range(0, 11):
        if p1[i] != p2[i]:
            return False
    return True


def energy(pattern, weights):
    energy = 0
    for i in range(0,11):
        for j in range(0,11):
            energy += (weights[i][j] * pattern[i] * pattern[j])
    return -1/2 * energy


        
submission=Submission("Finn_Hobson")
submission.header("Finn Hobson")

six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

weights = weight_matrix(three, six, one)

seven_segment(three)
print("Energy =", energy(three, weights))

seven_segment(six)
print("Energy =", energy(six, weights))

seven_segment(one)
print("Energy =", energy(one, weights))




##this assumes you have called your weight matrix "weights"
submission.section("Weight matrix")
submission.matrix_print("W",weights)

print()
print("test1")
submission.section("Test 1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]


seven_segment(test)
submission.seven_segment(test)
##for COMSM0027

##where energy is the energy of test
submission.print_number(energy(test, weights))

##this prints a space
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step

converged = False
while converged == False:
    updated_test = evolve_network(test, weights)
    converged = compare_patterns(test, updated_test)
    if converged == False:
        seven_segment(updated_test)
        submission.seven_segment(updated_test)
        print("Energy =", energy(updated_test, weights))
        submission.print_number(energy(updated_test, weights))
        submission.qquad()
        test = updated_test

print()
print("test2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
submission.section("Test 2")

seven_segment(test)


submission.seven_segment(test)

##for COMSM0027
##where energy is the energy of test
submission.print_number(energy(test, weights))

##this prints a space
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step

converged = False
while converged == False:
    updated_test = evolve_network(test, weights)
    converged = compare_patterns(test, updated_test)
    if converged == False:
        seven_segment(updated_test)
        submission.seven_segment(updated_test)
        print("Energy =", energy(updated_test, weights))
        submission.print_number(energy(updated_test, weights))
        submission.qquad()
        test = updated_test


submission.bottomer()



