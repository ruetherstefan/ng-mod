class PyTimer:
    def __init__(self, timeout, method_to_call, *args, **kwargs):
        import pygame

        self.run_time = timeout + pygame.time.get_ticks()

        self.method_to_call = method_to_call
        self.args = args
        self.kwargs = kwargs

    def run(self):
        import pygame

        if pygame.time.get_ticks() >= self.run_time:
            self.method_to_call(*self.args, **self.kwargs)
            return True
        else:
            return False
