from flask_restplus import Namespace, Resource, fields
from flask import request
from .lists.bubble_sort import bubble_sort

api = Namespace('Lists', description='List related operations')

lists = api.model('List', {
  'function': fields.String(description='The name of the operation'),
  'output': fields.String(description='The output of the operation')
})

class Output(object):
  def __init__(self, output, function):
    self.output = output
    self.function = function

@api.route('/bubble_sort', methods=['POST'])
@api.param('input', 'The list input', _in='body')
@api.response(404, 'Resource not found')
class BubbleSort(Resource):
  @api.doc('list_bubble_sort')
  @api.marshal_with(lists)
  def post(self):
    """
    Uses bubble sort on a list.

    Bubble_sort uses the technique of comparing and swapping.

    Function:
    ----------
    ```
    def bubble_sort(lst):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
    ```

    Examples:
    ----------
    ```
    morph.now.sh/lists/bubble_sort

    body: {
      "input": [1, 2, 3, 4, 5]
    }
    ```
    
    """
    req_data = request.get_json()
    input = req_data['input']
    output = bubble_sort(input)
    return Output(output=output, function='Bubble Sort')