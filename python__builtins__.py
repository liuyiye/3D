def py():
  import io
  print('lines:')
  mem_file=io.StringIO()
  while True:
    line=input()
    if line=='':break
    mem_file.write(line+'\n')
  code=mem_file.getvalue()
  exec(code)

while True:
  try:py()
  except Exception as e:print(e)
