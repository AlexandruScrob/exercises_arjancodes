

class PoolManager:
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.release(self.obj)


class Reusable:
    def test(self):
        print(f"Using object {id(self)}")


class ReusablePool:
    def __init__(self, size):
        self.size = size
        self.free = []
        self.in_use = []

        for _ in range(size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        if len(self.free) <= 0:
            raise Exception("No more objects are available")

        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)


pool = ReusablePool(2)
r = pool.acquire()
r2 = pool.acquire()

r.test()
r2.test()
pool.release(r2)
r3 = pool.acquire()
r3.test()

pool = ReusablePool(2)
with PoolManager(pool) as r:
    r.test()

with PoolManager(pool) as r:
    r.test()

with PoolManager(pool) as r:
    r.test()
