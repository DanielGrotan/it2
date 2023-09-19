Interval = tuple[float, float]


def intervals_overlap(interval1: Interval, interval2: Interval) -> bool:
    """Returns whether two intervals overlap with each other.

    Parameters
    ----------
    interval1 : Interval
        Inclusive interval (start, end)
    interval2 : Interval
        Inclusive interval (start, end)

    Returns
    -------
    bool
        Whether the intervals overlap
    """

    interval1_start, interval1_end = interval1
    interval2_start, interval2_end = interval2

    interval2_left_within = interval1_start <= interval2_start < interval1_end
    interval2_right_within = interval1_start < interval2_end <= interval1_end

    interval1_contained_within = (
        interval2_start <= interval1_start and interval1_end <= interval2_end
    )

    return interval2_left_within or interval2_right_within or interval1_contained_within


Box = tuple[float, float, float, float]


def boxes_overlap(box1: Box, box2: Box) -> bool:
    """Returns whether two boxes overlap with each other.

    Parameters
    ----------
    box1 : Box
        Top left and bottom right coordinates of the box (x1, y1, x2, y2)
    box2 : Box
        Top left and bottom right coordinates of the box (x1, y1, x2, y2)

    Returns
    -------
    bool
        Whether the boxes overlap
    """

    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2

    horizontal_overlap = intervals_overlap((x1, x2), (x3, x4))
    vertical_overlap = intervals_overlap((y1, y2), (y3, y4))

    return horizontal_overlap and vertical_overlap


def main() -> None:
    print("Kjører tester....")

    assert intervals_overlap((1, 3), (2, 4))
    assert intervals_overlap((2, 4), (1, 3))

    assert intervals_overlap((1, 3), (2, 3))
    assert intervals_overlap((2, 3), (1, 3))

    assert not intervals_overlap((3, 5), (7, 9))
    assert not intervals_overlap((7, 9), (3, 5))

    assert boxes_overlap((1, 1, 4, 4), (3, 0, 5, 2))
    assert boxes_overlap((3, 0, 5, 2), (1, 1, 4, 4))


if __name__ == "__main__":
    main()
