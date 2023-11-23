def arithmetic_arranger(problems, result=False):

  if len(problems) > 5:

    return 'Error: Too many problems.'

  else:

    l = []
    str1 = ''
    str2 = ''
    str_ = ''
    strr = ''

    for prob in problems:

      d = {}

      if '+' in prob:

        sp = prob.split(' + ')
        d['num1'] = sp[0]
        d['num2'] = sp[1]

        try:

          int(d['num1'])
          int(d['num2'])

        except:

          return 'Error: Numbers must only contain digits.'

        d['oper'] = '+'
        d['spacing'] = len(str(max(int(sp[0]), int(sp[1]))))

        if result:

          d['result'] = str(int(sp[0]) + int(sp[1]))

      elif '-' in prob:

        sp = prob.split(' - ')
        d['num1'] = sp[0]
        d['num2'] = sp[1]

        try:

          int(d['num1'])
          int(d['num2'])

        except:

          return 'Error: Numbers must only contain digits.'

        d['oper'] = '-'
        d['spacing'] = len(str(max(int(sp[0]), int(sp[1]))))

        if result:

          d['result'] = str(int(sp[0]) - int(sp[1]))

      else:

        return "Error: Operator must be '+' or '-'."

      if d['spacing'] > 4:

        return 'Error: Numbers cannot be more than four digits.'

      l.append(d)

    for e in l:

      str1 += 2 * ' ' + (e['spacing'] -
                         len(e['num1'])) * ' ' + e['num1'] + 4 * ' '
      str2 += e['oper'] + ' ' + (e['spacing'] -
                                 len(e['num2'])) * ' ' + e['num2'] + 4 * ' '
      str_ += (e['spacing'] + 2) * '-' + 4 * ' '

      if result:

        strr += (e['spacing'] + 2 -
                 len(e['result'])) * ' ' + e['result'] + 4 * ' '

    string = str1[:-4] + '\n' + str2[:-4] + '\n' + str_[:-4]

    if result:

      string += '\n' + strr[:-4]

    return string
