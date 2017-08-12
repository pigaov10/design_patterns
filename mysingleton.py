class Singleton(object):
  def __new__(cls):
    if not hasattr(cls, 'obj'):
    	cls.obj = super(Singleton, cls).__new__(cls)
    print cls.obj
    return cls.obj

if __name__ == '__main__':
  c1 = Singleton()
  c2 = Singleton()
  print c1
  print c2
