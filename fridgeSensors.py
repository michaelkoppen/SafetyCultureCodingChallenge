def main():
    fridgeSensorData = [{"id": "a", "timestamp": 1509493641, "temperature": 3.53},
                        {"id": "b", "timestamp": 1509493642, "temperature": 4.13},
                        {"id": "c", "timestamp": 1509493643, "temperature": 3.96},
                        {"id": "a", "timestamp": 1509493644, "temperature": 3.63},
                        {"id": "c", "timestamp": 1509493645, "temperature": 3.96},
                        {"id": "a", "timestamp": 1509493645, "temperature": 4.63},
                        {"id": "a", "timestamp": 1509493646, "temperature": 3.53},
                        {"id": "b", "timestamp": 1509493647, "temperature": 4.15},
                        {"id": "c", "timestamp": 1509493655, "temperature": 3.95},
                        {"id": "a", "timestamp": 1509493677, "temperature": 3.66},
                        {"id": "b", "timestamp": 1510113646, "temperature": 4.15},
                        {"id": "c", "timestamp": 1510127886, "temperature": 3.36},
                        {"id": "c", "timestamp": 1510127892, "temperature": 3.36},
                        {"id": "a", "timestamp": 1510128112, "temperature": 3.67},
                        {"id": "b", "timestamp": 1510128115, "temperature": 3.88}]

    # Dictionary to be filled with lists of temperatures for each of the fridges.
    temperatures = {}

    # Loops through fridgeSensorData and adds each fridge and it's temperature list to the temperatures dictionary.
    for fridge in fridgeSensorData:
        if (fridge["id"]) not in temperatures:
            temperatures[fridge["id"]] = [fridge["temperature"]]
        else:
            temperatures[fridge["id"]].append(fridge["temperature"])

    # Calculates averages and appends to averages dictionary.
    averages = calculateAverages(temperatures)

    # Calculates medians and appends to medians dictionary.
    medians = calculateMedians(temperatures)

    # Calculates modes and appends to modes dictionary.
    modes = calculateModes(temperatures)

    # Calculates modes and appends to modes dictionary.
    output = createOutput(temperatures, averages, medians, modes)

    # Prints output JSON array with each element on a new line.
    print("[", end="")
    for id in output:
        if id == output[-1]:
            print(id, end="")
            print("]")
        else:
            print(id, end="")
            print(",")

    # Pauses program so that the output can be displayed. User can press enter to then close the program.
    input()


def calculateAverages(temperatures):
    """
    Takes temperatures dictionary and calculates the averages for each id and returns an averages dictionary.
    :param temperatures: 
    :return averages: 
    """
    averages = {}
    for id, temps in temperatures.items():
        averages[id] = round(sum(temps) / len(temps), 2)
    return averages


def calculateMedians(temperatures):
    """
    Takes temperatures dictionary and calculates the medians for each id and returns a medians dictionary.
    :param temperatures: 
    :return medians: 
    """
    medians = {}
    for id, temps in temperatures.items():
        temperatures[id].sort()
        half = len(temps) // 2
        # Checks if temperature's list has an even or odd length and determines median based on this.
        if int(len(temps)) % 2 == 0:
            medians[id] = round((temps[half] + temps[half - 1]) / 2, 2)
        else:
            medians[id] = round(temps[half], 2)
    return medians


def calculateModes(temperatures):
    """
    Takes temperatures dictionary and calculates the modes for each id and returns a modes dictionary.
    :param temperatures: 
    :return modes: 
    """
    modes = {}
    for id, temps in temperatures.items():
        counts = {}
        modes[id] = []
        # Fills counts dictionary with number of instances of each temperature.
        for temperature in temps:
            if temperature not in counts:
                counts[temperature] = 1
            else:
                counts[temperature] += 1

        # Checks if any other temperatures are equally as common as mostCommonTemperature and appends them to the
        # modes dictionary as a list.
        mostCommonTemperature = max(counts.values())
        for temperature, count in counts.items():
            if count == mostCommonTemperature:
                modes[id].append(round(temperature, 2))
    return modes


def createOutput(temperatures, averages, medians, modes):
    """
    Takes averages, medians and modes dictionaries and returns the final JSON array.
    :param averages: 
    :param medians: 
    :param modes: 
    :return output: 
    """
    output = []
    for id in temperatures:
        average = averages[id]
        median = medians[id]
        mode = modes[id]
        output.append({"id": id, "average": average, "median": median, "mode": mode})
    return output


if __name__ == '__main__':
    main()
