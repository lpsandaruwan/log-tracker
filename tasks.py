"""
Tasks
Tasks on resource connections.

11/04/2017 lpsandaruwan <http://lahiru.site>
"""


def example_function(text_stream):
    # prepare text stream object
    text_stream.load()

    # tail log file, equals to tail -f in unix
    for line in text_stream.tail():
        print(line.rstrip("\n"))
