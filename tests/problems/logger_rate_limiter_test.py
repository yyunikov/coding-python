from src.problems.logger_rate_limiter import Logger


def test_logger():
    logger = Logger()

    assert logger.shouldPrintMessage(1, "foo")
    assert logger.shouldPrintMessage(2, "bar")
    assert not logger.shouldPrintMessage(3, "foo")
    assert not logger.shouldPrintMessage(8, "bar")
    assert not logger.shouldPrintMessage(10, "foo")
    assert logger.shouldPrintMessage(11, "foo")
