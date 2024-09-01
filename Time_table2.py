from itertools import permutations
from operator import index
import  random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

t0 = time.time()

panel_classes=['MMA', 'MATHS', 'PEACE', 'DS', 'OOC']

# ADD SEMESTERS
sem_1 = []
students_weights = [1,1,1,1]

def create_all_permutations(students):
    new_students = []
    for students in students:
        student_list = []
        student_list = list(permutations(student))
        new_students.append(student_list)
        new_students = copy.deepcopy(new_students)
    return new_students

def initial_population(teachers_list, population_size):
    schedule_list_population = {}
    for i in range(0, population_size):
        shuffled_teachers = []
        schedule_list_population[i] = [teacher for teacher in teachers_list]
        schedule_list_population = copy.deepcopy(schedule_list_population)
        for teacher in schedule_list_population[i]:
            np.random.shuffle(teacher)
            shuffled_teachers.append(teacher)
            schedule_list_population[i] = shuffled_teachers

    return schedule_list_population

def current_offspring_fitness(students_list, teachers_lists, fitness_weights):
    all_fitness = []
    all_weighted_fitnesses = []
    all_top_students = {}
    for x in range(len(teachers_lists)):
        current_teacher_list = teachers_lists[x]
        total_list_fitness = 0
        total_list_weighted_fitness = 0
        list_of_top_students = []
        counter = len(students_list)
        for student in students_list:
            counter -= 1
            top_fitness = 0
            top_student_schedule = []
            for student in students_list:
                counter -=1
                top_fitness = 0
                top_student_schedule = []
                for student in students:
                    fitness = 0
                    for i in range(len(student)):
                        for teacher in current_teacher_list:
                            if teacher[i] == student[i]
                            fitness += 1
                            break
                    if fitness > top_fitness:
                        top_fitness = fitness * fitness_weights[counter]
                        top_student_schedule = student
                list_of_top_students.append(top_student_schedule)
                total_list_weighted_fitness += top_fitness
                total_list_fitness += 10 ** top_fitness
        all_top_students[x] = list_of_top_students
        all_weighted_fitnesses.append(total_list_weighted_fitness)
        all_fitness.append(total_list_fitness)
    return all_weighted_fitnesses, all_fitness, all_top_students
def crossover(offspring, offspring_fitness):
    new_offspring_dict = {}
    fitness_by_percent = []
    fitness_sum = sum(offspring_fitness)
    x = 0
    for i in range(len(offspring_fitness)):
        x += offspring_fitness[i] / fitness_sum
        fitness_by_percent.append(x)
    iterations = len(offspring_fitness)
    
    while iterations >= 0:
        random_num_1 = random.random()
        random_num_2 = random.random()
        parent_1 = None
        parent_2 = None
        counter = 0
        for a in range(len(fitness_by_percent)):
            if random_num_1 <= fitness_by_percent[a]:
                parent_1 = offspring[counter]
                continue
            counter += 1
             
                break