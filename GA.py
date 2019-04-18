# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:17:50 2019

@author: xy
"""

#This script is used to write a GA which is uesd to generate picture by using 100 traingles.
from PIL import Image,ImageDraw
import random


class triangle():
    def __init__(self,point1 = (0,0),point2=(0,1),point3=(1,0),rgb=(255,255,255)):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.rgb = rgb

class chromosome():
    def __init__(self,width,height):
        self.num = 100 #一个染色体里三角形的个数
        self.triangles=[]
        for i in range(0,self.num):
            point1x = random.randint(0,width-1)
            point1y = random.randint(0,height-1)
            point2x = random.randint(0,width-1)
            point2y = random.randint(0,height-1)
            point3x = random.randint(0,width-1)
            point3y = random.randint(0,height-1)
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            self.triangles.append(triangle((point1x,point1y),(point2x,point2y),(point3x,point3y),(r,g,b)))
     
     
    def draw(self,width,height):
         self.im = Image.new('RGB',(width,height),(0,0,0))
         
         for triangle in self.triangles:
             temp_im = Image.new('RGB',(width,height),(0,0,0))
             imDraw = ImageDraw.Draw(temp_im)
             imDraw.polygon([triangle.point1,triangle.point2,triangle.point3],triangle.rgb)
             
             for i in range(0,width):
                 for j in range(0,height):
                     new_point = temp_im.getpixel((i,j))
                     orignal_point = self.im.getpixel((i,j))
                     if new_point[0]!=0 or new_point[1]!=0 or new_point[2]!=0 :
                         alpha=0.5
                         #alpha0 = float(orignal_point[3])/255
                         #alpha1 = float(new_point[3])/255
                         res_point = (int(orignal_point[0]*(1-alpha)+new_point[0]*alpha),\
                                      int(orignal_point[1]*(1-alpha)+new_point[1]*alpha),\
                                      int(orignal_point[2]*(1-alpha)+new_point[2]*alpha),\
                                      )
                         self.im.putpixel((i,j),res_point)
            
            # self.im = Image.blend(self.im,temp_im,0.5)
        # self.im.show()
    def calFit(self,target):
        width = target.width
        height = target.height
        fitness = 0
        for i in range(0,width):
            for j in range(0,height):
                target_point = target.getpixel((i,j))
                this_point = self.im.getpixel((i,j))
                length = len(target_point)
                for k in range(0,length):
                    fitness += abs(this_point[k]-target_point[k])
        self.fitness = float(4*width*height)/fitness
        
class GA():
    
    def __init__(self):
        self.num = 16
        self.cross_rate = 0.86
        self.mut_rate = 0.1
        self.chromosomes = []
        self.target = Image.open('firefox.png')
        self.target = self.target.resize((32,32))
        self.width = self.target.width
        self.height = self.target.height
        self.iter_num = 5000
        self.interval = 10
        self.count = 1
        for i in range(self.num):
            self.chromosomes.append(chromosome(self.width,self.height))
        
        
    def crossover(self):
        unselected = [i for i in range(self.num)]
        while len(unselected)!=0:
            pos1 = random.choice(unselected)
            unselected.remove(pos1)
            pos2 = random.choice(unselected)
            unselected.remove(pos2)
            if random.random() < self.cross_rate:
                triangle_num = self.chromosomes[pos1].num
                for i in range(triangle_num):
                    if random.randint(0,10) % 2 == 0:
                        temp_triangle = self.chromosomes[pos1].triangles[i]
                        self.chromosomes[pos1].triangles[i] = self.chromosomes[pos2].triangles[i]
                        self.chromosomes[pos2].triangles[i] = temp_triangle
    def update(self):
        chromosome_num = self.num
        for i in range(chromosome_num):
            self.chromosomes[i].draw(self.width,self.height)
            self.chromosomes[i].calFit(self.target)
            
    def selection(self):
        '''
        sum_fit_value = 0;
        chromosome_num = self.num
        for i in range(chromosome_num):
            sum_fit_value += self.chromosomes[i].fitness
        accProbability = [0 for i in range(chromosome_num)]
        for i in range(chromosome_num):
            accProbability[i] += self.chromosomes[i].fitness/sum_fit_value
            if i > 0:
                accProbability[i]+=accProbability[i-1]
        new_chromosomes = []
        for i in range(chromosome_num):
            rand = random.random()
            for j in range(chromosome_num):
                if accProbability[j]>=rand:
                    new_chromosomes.append(self.chromosomes[j])
                    break
        self.chromosomes = new_chromosomes
        '''
        min_pos = 0
        min_fit = 100
        for i in range(self.num):
            if self.chromosomes[i].fitness<min_fit:
                min_fit = self.chromosomes[i].fitness
                min_pos = i
        second_min_pos = 0
        second_min_fit = 100
        for i in range(self.num):
            if i!=min_pos and self.chromosomes[i].fitness<second_min_fit:
                second_min_fit = self.chromosomes[i].fitness
                second_min_pos = i
                
        '''
        rand_pos1 = random.randint(0,self.num-1)
        while rand_pos1 == min_pos or rand_pos1 == second_min_pos:
            rand_pos1 = random.randint(0,self.num-1)
        
        rand_pos2 = random.randint(0,self.num-1)
        while rand_pos2 == min_pos or rand_pos2 == second_min_pos:
            rand_pos2 = random.randint(0,self.num-1)
        '''
        best_pos = 0
        best_fitness = 0
        for i in range(self.num):
            if self.chromosomes[i].fitness > best_fitness:
                best_fitness = self.chromosomes[i].fitness
                best_pos = i
        second_best_pos = 0
        second_best_fit = 0
        for i in range(self.num):
            if i!=best_pos and self.chromosomes[i].fitness > second_best_fit:
                second_best_fit = self.chromosomes[i].fitness
                second_best_pos = i
        
        for i in range(self.chromosomes[0].num):
            if random.random()>0.86:
                self.chromosomes[min_pos].triangles[i] = self.chromosomes[best_pos].triangles[i]
                self.chromosomes[second_min_pos].triangles[i] = self.chromosomes[second_best_pos].triangles[i]
            else:
                self.chromosomes[min_pos].triangles[i] = self.chromosomes[second_best_pos].triangles[i]
                self.chromosomes[second_min_pos].triangles[i] = self.chromosomes[best_pos].triangles[i]
    def mutation(self):
        chromosome_num = self.num
        for i in range(chromosome_num):
            rand = random.random()
            if rand < self.mut_rate:
                mut_pos = random.randint(0,self.chromosomes[0].num-1)
                point1x = random.randint(0,self.width-1)
                point1y = random.randint(0,self.height-1)
                point2x = random.randint(0,self.width-1)
                point2y = random.randint(0,self.height-1)
                point3x = random.randint(0,self.width-1)
                point3y = random.randint(0,self.height-1)
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                self.chromosomes[i].triangles[mut_pos] = triangle((point1x,point1y),(point2x,point2y),(point3x,point3y),(r,g,b))
    def save_best(self):
        best_pos = 0
        best_fitness = 0
        for i in range(self.num):
            if self.chromosomes[i].fitness > best_fitness:
                best_fitness = self.chromosomes[i].fitness
                best_pos = i
        name = 'firefox\\第'+str(self.count)+'轮最好结果'+str(best_fitness)+'.png'
        self.chromosomes[best_pos].im.save(name)
    #def selection(self):
    def run(self):
        while self.count < self.iter_num:
            self.update()
            if self.count % self.interval == 0:
                self.save_best()
            self.selection()
            self.crossover()
            self.mutation()
            
            print('目前是第'+str(self.count)+'轮')
            self.count+=1
            
        
ga = GA()
ga.run()