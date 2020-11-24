import pytest

from queue_with_stacks.queue_with_stacks import PseudoQueue, InvalidOperationError


def test_enqueue():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.stack1.top.value
    expected = "apple"
    assert actual == expected


def test_dequeue():
    q = PseudoQueue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


def test_peek():
    q = PseudoQueue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.stack1.peek()
    expected = "apple"
    assert actual == expected


def test_peek_when_empty():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError):
        q.stack1.peek()


def test_enqueue_one():
    q = PseudoQueue()
    q.enqueue("apples")
    actual = q.stack1.peek()
    expected = "apples"
    assert actual == expected


def test_enqueue_two():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.stack1.peek()
    expected = "apples"
    assert actual == expected


def test_dequeue_when_empty():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()


def test_dequeue_when_full():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


def test_peek_post_dequeue():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.stack1.peek()
    expected = "bananas"
    assert actual == expected


def test_is_empty():
    q = PseudoQueue()
    actual = q.stack1.is_empty()
    expected = True
    assert actual == expected


def test_exhausted():
    q = PseudoQueue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.stack1.is_empty()
    expected = True
    assert actual == expected