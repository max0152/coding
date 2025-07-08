class math:
  @staticmethod
  def fac(n):
    if n == 0:
        return 1
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

  @staticmethod
  def step(base, exponent):
    result = base ** exponent
    print(result)

  @staticmethod
  def form(n):
    return n + 1
    
