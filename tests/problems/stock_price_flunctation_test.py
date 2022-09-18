import pytest

from src.problems.stock_price_flunctation import StockPrice


@pytest.mark.parametrize(
    "function_call,args,result",
    [
        (["update", "update", "current", "maximum", "update",
          "maximum", "update", "minimum"],
         [[1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []],
         [None, None, 5, 10, None, 5, None, 2]
         ),
        (["update", "maximum", "current", "minimum", "maximum", "maximum",
          "maximum", "minimum", "minimum", "maximum", "update", "maximum",
          "minimum", "update", "maximum", "minimum", "current", "maximum",
          "update", "minimum", "maximum", "update", "maximum", "maximum",
          "current", "update", "current", "minimum", "update", "update",
          "minimum", "minimum", "update", "current", "update", "maximum",
          "update", "minimum"],
         [[38, 2308], [], [], [], [], [], [], [], [], [], [47,
                                                           7876], [], [], [
              58, 1866], [], [], [], [], [43, 121], [], [], [40,
                                                             5339], [], [], [],
          [
              32, 5339], [], [], [43, 6414], [49, 9369], [], [], [36,
                                                                  3192], [], [
              48, 1006], [], [53, 8013], []],
         [
             None, 2308, 2308, 2308, 2308, 2308, 2308, 2308, 2308, 2308,
             None, 7876, 2308, None, 7876, 1866, 1866, 7876, None, 121, 7876,
             None, 7876, 7876, 1866, None, 1866, 121, None, None, 1866, 1866,
             None, 1866, None, 9369, None, 1006]

         ),
        ([
             "update", "maximum", "current", "minimum", "update", "update",
             "maximum", "current", "current", "minimum", "minimum", "maximum",
             "current", "maximum", "current", "maximum", "update", "minimum",
             "current", "current", "maximum", "update", "minimum", "maximum",
             "minimum", "minimum", "update", "maximum", "update", "maximum",
             "current", "current", "maximum", "maximum", "minimum", "update",
             "update", "maximum", "update", "current", "minimum", "minimum",
             "maximum", "minimum", "maximum", "update", "update", "minimum",
             "update", "current", "maximum"],
         [[63, 7626], [], [], [], [87, 9207], [47,
                                               8547], [], [], [], [], [], [],
          [], [], [], [], [
              93, 4215], [], [], [], [], [87, 2453], [], [], [], [], [65,
                                                                      9645],
          [], [
              44, 7696], [], [], [], [], [], [], [70, 2959], [33, 393], [],
          [77,
           7333], [], [], [], [], [], [], [
              62, 7696], [29, 3348], [], [75, 3348], [], []],
         [None, 7626, 7626, 7626, None, None, 9207, 9207, 9207, 7626,
          7626, 9207, 9207, 9207, 9207, 9207, None, 4215, 4215, 4215, 9207,
          None, 2453, 8547, 2453, 2453, None, 9645, None, 9645, 4215, 4215,
          9645, 9645, 2453, None, None, 9645, None, 4215, 393, 393, 9645, 393,
          9645, None, None, 393, None, 4215, 9645]),
    ]
)
def test_stock_price(function_call, args, result):
    stock_price = StockPrice()

    for i in range(0, len(function_call)):
        if function_call[i] == "update":
            stock_price.update(args[i][0], args[i][1])
        else:
            func = getattr(stock_price, function_call[i])
            assert func() == result[i]
