class Employee:

    def _init_(self, name, gender, age, id, job, salary):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__id = id
        self.__job = job
        self.__salary = salary


    def _setName_(self, name):
        self.__name = name


    def _getName_(self):
        return self.__name


    def _setGender_(self, g):
        self.__gender = g


    def _getGender_(self):
        return self.__gender


    def _setAge_(self, age):
        self.__age = age


    def _getAge_(self):
        return self.__age


    def _setID_(self, id):
        self.__id = id


    def _getID_(self):
        return self.__id


    def _setJob_(self, job):
        self.__job = job


    def _getJob_(self):
        return self.__job


    def _setSalary_(self, salary):
        self.__salary = salary


    def _getSalary_(self):
        return self.__salary


    def _str_(self):
        return "Name:{}, Age:{} ,ID: {},Job: {},Salary: {}".format(self._name, self.age, self.id, self.job,self._salary)