class Sol:
    def sqrt(self,initial_x):
        for i in range(10):
            if i==0:
                current_x=initial_x
            f=current_x**2-initial_x
            next_x=current_x-(f/(current_x*2))
            current_x=next_x
        return next_x
if __name__ == '__main__':
    initial_x=2
    p1=Sol()
    print(p1.sqrt(initial_x))
