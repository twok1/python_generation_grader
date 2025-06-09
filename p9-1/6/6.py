class HighScoreTable:
  def __init__(self, length):
    self.length = length
    self.scores = []
    
  def update(self, score):
    self.scores.append(score)
    self.scores = list(reversed(sorted(self.scores)))
    if len(self.scores) > self.length:
      self.scores = self.scores[:self.length]
    
  
  def reset(self):
    self.scores = []
  