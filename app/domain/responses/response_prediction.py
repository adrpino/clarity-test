from flask import jsonify

class ResponsePrediction:

    @staticmethod
    def create(score):
        if not isinstance(score, (int, float)):
            raise TypeError('score should be a number, not a %s' % type(score))
        if not 0 <= score <= 1:
            raise ValueError('score should be between 0 and 1')

        response = {
            'score': score,
        }
        return jsonify(response)