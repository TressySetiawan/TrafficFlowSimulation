class TrafficSignal:
    def __init__(self, roads, k, config={}):
        # Initialize roads
        self.roads = roads
        # Set default configuration
        self.set_default_config(k)
        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()

    def set_default_config(self, k):
        self.traf_k = k
        if k == 4:
            self.cycle = [(True, False, False, False), (False, True, False, False), (False, False, True, False), (False, False, False, True)]
        elif k == 3 :
            self.cycle = [(True, False, False), (False, True, False), (False, False, True)]
        else :
            self.cycle = [(True, False), (True, False)]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 15

        self.current_cycle_index = 0

        self.last_t = 0

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]
    
    def update(self, sim):
        cycle_length = 10
        k = (sim.t // cycle_length) % self.traf_k
        self.current_cycle_index = int(k)
