int x;
    int y;
    void setValues(int a, int b)
    {
        x=a;
        y=b;
    }
    int getSum()
    {
        return x+y;
    }
    int getDifference()
    {
        return x-y;
    }
    int getProduct()
    {
        return x*y;
    }
    int getQuotient()
    {
        return x/y;
    }
    int getRemainder()
    {
        return x%y;
    }
    int getPower()
    {
        
        return (int)Math.pow(x,y);
    }
