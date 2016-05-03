

class DataSample:
    def __init__(self, inputs, outputs, inputs_ranges, output_range):
        self.inputs = inputs
        self.outputs = outputs
        self.inputs_ranges = inputs_ranges
        self.output_range = output_range

    def print_details(self):
        print "inputs: " + str(self.inputs)
        print "outputs: " + str(self.outputs)
        #print "input ranges: " + self.inputs
        #print "inputs: " + self.inputs
