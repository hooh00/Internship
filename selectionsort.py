class Main :
    @staticmethod
    def main( args) :
        entries = [3, 6, 1, 8, 0, 2, 4]
        Main.selectionSort(entries)
    @staticmethod
    def selectionSort( values) :
        i = 0
        while (i < len(values) - 1) :
            smallest = i
            j = i
            while (j < len(values)) :
                if (values[j] < values[smallest]) :
                    smallest = j
                j += 1
            # swapping
            temp = values[smallest]
            values[smallest] = values[i]
            values[i] = temp
            i += 1
        # testing purposes (print)
        i = 0
        while (i < len(values)) :
            print(str(values[i]) + " ", end ="")
            i += 1
    

if __name__=="__main__":
    Main.main([])
