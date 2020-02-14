# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(items):
    if len(items) <= 1:
        return True
    else:
        for index in range(len(items)):
            if index == 0 or items[index] > items[index - 1]:
                pass
            else:
                return False
        return True

def riffle(items, out):
    riffledList = []

    for x,y in zip(items[:len(items)//2], items[len(items)//2:]):
        if out:
            riffledList.append(x)
            riffledList.append(y)
        else:
            riffledList.append(y)
            riffledList.append(x)
    return riffledList

def only_odd_digits(n):
    for num in str(n):
        if int(num) % 2 != 1:
            return False
        else:
            pass
    return True

def pyramid_blocks(n, m, h):
    numberOfBlocks = 0
    for _ in range(h):
        numberOfBlocks += n*m
        n +=1
        m +=1
    return numberOfBlocks

def is_cyclops(n):
    return not(len(str(n)) % 2 != 1 or str(n).count('0') != 1 or int(str(n)[len(str(n))//2]) != 0)

def domino_cycle(tiles):
    if len(tiles) < 1:
        return True
    else:
        for index, tile in enumerate(tiles):
            if index != len(tiles) - 1:
                if tile[0] == tiles[index - 1][1] and tile[1] == tiles[index + 1][0]:
                    pass
                else:
                    return False
            else: #if its the last tile we need to make sure it wraps around to check against the first
                if tile[0] == tiles[index - 1][1] and tile[1] == tiles[0][0]:
                    pass
                else:
                    return False
    return True

def count_dominators(items):
  highestNumber = 0
  count = 0
  ##if we do our comparisons backwards we can check against previously checked digits, cutting down the time
  for num in reversed(items):
      if num > highestNumber:
        highestNumber = num
        count += 1
  return count

def extract_increasing(digits):
  listOfIncreasingDigits = []
  counterDigit = ''
  for digit in digits:
    if len(listOfIncreasingDigits) == 0 or  int(counterDigit + digit) > listOfIncreasingDigits[-1]:
      listOfIncreasingDigits.append(int(counterDigit + digit))
      counterDigit = ''
    else:
      counterDigit += digit
  return listOfIncreasingDigits

def words_with_letters(words, letters):
    wordsThatMatch = []
    j, i = 0, 0
    for word in words:
        while and j < len(letters) and i < len(word):
            if letters[j] == word[i]:
                if j != len(letters) - 1:
                    j += 1
                else:
                    wordsThatMatch.append(word)
                    break
            else:
                i += 1
        j, i = 0, 0
        pass
    return wordsThatMatch

