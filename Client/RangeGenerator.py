# RangeGenerator class will contain the method that helps us
# generate range of integers according to input.
class RangeGenerator:

    # The generateRange is responsible for generating a range of integers
    # according to input, it is a static method we can call without creating an instance of the class.
    @staticmethod
    def generateRange(rangeSet):
        try:
            # rangeSet is the tuple or list that contains the start and the 
            # end of the range of integers that will be generated.
            start, end = rangeSet

            # We generate a range of integers from start to end(including end)
            # and is returned in the form of set.
            return set(range(start, end + 1))
        
        except TypeError:
            # Here we handle the exception where the rangeSet is not a tuple or list 
            # (Varaible is not of the Type required).
            print("Invalid input: rangeSet must be a tuple or list.")

            # Return an empty set in case of an exception.
            return set()
        
        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            print(f"An unexpected error occurred during range generation: {e}")
            
            # Return an empty set in case of an exception.
            return set()