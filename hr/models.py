from django.db import models

# Create your models here.

# select_related() - нужно использовать когда мы будет получать всех сотрудников вместе с отношениями других таблиц он делает 1 запрос и получает данные со всех таблиц привязанные к родительской
#1) Потомучто мы зделаем 1 запрос для получение всех сотрудников и потмо через цикл будем получать все их данные из других ьаблиц если такие имеются

#Many to Many (Многие-ко-многим)
class Compensation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#One to One  (один-к-одному) Данный тип связи создаёт еще одну таблицу а родителский класс создает поле где указывается id на поле дочернего класса
# обращение 
class Contact(models.Model):# Дочерний
    phone = models.CharField(max_length=50, unique=False, verbose_name="Телефон")
    address = models.CharField(max_length=50, verbose_name="Адресс")

    def __str__(self):
        return self.phone 
    
#ForeignKey (один-ко-многим)
#Обращение:
# depart = Department.objects.create(name="IT", description="IT for monkeys") Создаём новый депортамент
# employee_it.department = depart Засовываем работника в этот департамент
# employee.depart.name, description получаем данные о департаменте от сотрудника
# depart.employee_set.all() покажит все данные в это таблице employee_set это стандартное джанговское related_name название класса в нижнем регистре и мы может это сами переопределить -|
class Department(models.Model):# Дочерний                                                                                                                                               |                                                                           
    name = models.CharField(max_length=255, verbose_name="Имя отдела")#                                                                                                                 |
    description = models.TextField(blank=True, null=True)#                                                                                                                              |
#                                                                                                                                                                                       |
    def __str__(self):#                                                                                                                                                                 |
        return self.name#                                                                                                                                                               |
#                                                                                                                                                                                       |
#Обращение employee = Employee.objects.create(first_name="Floppy", last_name="Disk")                                                                                                    |
class Employee(models.Model):# Родительский                                                                                                                                             |
    first_name = models.CharField(max_length = 150)#                                                                                                                                    |
    last_name = models.CharField(max_length=150)#                                                                                                                                       |
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)#                 переопределение |-----------------------------------------------------------------------
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, null=True, related_name="employ_boy") # Нужен специально для того чтобы переопределить название employee_set где employee это наша таблица в нижен регистре
    compensation = models.ManyToManyField(Compensation)
    class Meta:
        db_table = "employe"
    