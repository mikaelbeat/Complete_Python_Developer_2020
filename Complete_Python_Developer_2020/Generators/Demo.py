
# Generator functions use yield instead of return

# The yield statement suspends function’s execution and sends a value back to the caller, 
# but retains enough state to enable function to resume where it is left off. When resumed, 
# the function continues execution immediately after the last yield run. This allows 
# its code to produce a series of values over time, rather than computing them at once 
# and sending them back like a list.

def generator_function(num):
    for i in range(num):
        yield i * 2

g = generator_function(10)

print(f"Calculates 0 * 2 -> {next(g)}")
print(f"Calculates 1 * 2 -> {next(g)}")
print(f"Calculates 2 * 2 -> {next(g)}")
print(f"Calculates 3 * 2 -> {next(g)}")
print(f"Calculates 4 * 2 -> {next(g)}")