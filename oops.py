
class GF:
    def fun(self):
        print("hello")
        
        
class F(GF):
    def fun(self):
        print("hey")   
    def mr(self):
     super().fun()
        
        
soumya = F()
soumya.mr()