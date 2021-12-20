import copy
import time
from collections import deque
from heapq import heappop, heappush
from typing import List, Optional, Tuple


class Bucket:
    def __init__(self, ball_list: List[int]) -> None:
        """Bucketを初期化

        Args:
            ball_list (int): 長さ2のリスト
        """

        if len(ball_list) != 2:
            raise ValueError
        self.ball_list = ball_list


class BucketCollection:
    def __init__(self, bucket_list: List[Bucket]) -> None:
        """BucketCollectionを初期化

        Args:
            bucket_list (List[Bucket]): バケツをリストにして渡す．
        """

        self.bucket_list = bucket_list
        self.length = len(bucket_list)

    def swap(self, bucket_left: int, ball_in_left_bucket: int, ball_in_right_bucket: int) -> "BucketCollection":
        """ボールを交換し，新たなBucketCollectionを返す

        Args:
            bucket_left (int): 交換するバケツの左側を指定．0 ~ n-2
            ball_in_left_bucket (int): 左側のバケツのどのボールを交換するか指定．0 or 1
            ball_in_right_bucket (int): 右側のバケツのどのボールを交換するか指定．0 or 1
        """

        copy_bucket_list = copy.deepcopy(self.bucket_list)
        left_ball = self.bucket_list[bucket_left].ball_list[ball_in_left_bucket]
        right_ball = self.bucket_list[bucket_left + 1].ball_list[ball_in_right_bucket]
        copy_bucket_list[bucket_left + 1].ball_list[ball_in_right_bucket], copy_bucket_list[bucket_left].ball_list[ball_in_left_bucket] = left_ball, right_ball
        return BucketCollection(bucket_list=copy_bucket_list)

    @property
    def get_ball_state(self) -> Tuple[int, ...]:
        """BucketCollectionからボールをリストにして返す

        Returns:
            Tuple[int]: ボールをリストにして返す
        """

        ball_state = []
        for i in range(self.length):
            ball_state.append(self.bucket_list[i].ball_list[0])
            ball_state.append(self.bucket_list[i].ball_list[1])
        return tuple(ball_state)


class Node:
    def __init__(self, bucket_collection: BucketCollection, pre_node: Optional["Node"]) -> None:
        """前回の状態と，今回の状態を保持

        Args:
            bucket_collection (BucketCollection): 今回のBucketCollection
            pre_node (Node): 親ノード
        """

        self.bucket_collection = bucket_collection
        self.pre_node = pre_node

    @property
    def action(self) -> str:
        """前回と今回のBucketCollectionから，起こしたアクションを返す

        Returns:
            str: 起こしたアクションを返す (例. 1 <-> 2)
        """
        # pre_nodeがNoneの時はactionは無い
        assert self.pre_node is not None
        pre_bucket_collection = self.pre_node.bucket_collection
        for i in range(self.bucket_collection.length):
            if self.bucket_collection.bucket_list[i].ball_list != pre_bucket_collection.bucket_list[i].ball_list:
                break
        # pythonではfor文のiが保存されている
        return f'{i+1} <-> {i+2}'

    @property
    def score(self) -> int:
        """最終状態までの推定コストを返す
        """

        score = 0
        for i in range(self.bucket_collection.length):
            score += abs(i+1 - self.bucket_collection.bucket_list[i].ball_list[0])
            score += abs(i+1 - self.bucket_collection.bucket_list[i].ball_list[1])
        return score

    def print_bucket_collection(self) -> None:
        """今回のBucketCollectionをprintする
        """

        for bucket in self.bucket_collection.bucket_list:
            print(bucket.ball_list)

    def __le__(self, other: "Node"):
        return self.score <= other.score

    def __ge__(self, other: "Node"):
        return self.score >= other.score

    def __lt__(self, other: "Node"):
        return self.score < other.score

    def __gt__(self, other: "Node"):
        return self.score > other.score

    def __qe__(self, other: "Node"):
        return self.score == other.score


class BucketPuzzleSolver:
    def __init__(self, bucket_num: int) -> None:
        """BucketPuzzleSolverを初期化

        Args:
            bucket_num (int): バケツの数を指定
        """
        self.bucket_num = bucket_num

    def reset(self) -> None:
        self.initial_bucket_collection = BucketCollection(bucket_list=list(Bucket(ball_list=[bucket_num - i, bucket_num - i]) for i in range(bucket_num)))
        self.initial_node = Node(bucket_collection=self.initial_bucket_collection, pre_node=None)
        self.goal_bucket_collection = BucketCollection(bucket_list=list(Bucket(ball_list=[i + 1, i + 1]) for i in range(bucket_num)))

    def is_goal(self, bucket_collection: BucketCollection) -> bool:
        """バケツパズルが解けているか判定

        Args:
            bucket_collection (BucketCollection): 判定するBucketCollection

        Returns:
            bool: バケツパズルが解けているか
        """
        if bucket_collection.get_ball_state == self.goal_bucket_collection.get_ball_state:
            return True
        return False

    def bfs_solver(self, do_print: bool) -> Tuple[List["Node"], int, float]:
        """バケツパズルBFSで解く

        Args:
            do_print (bool): Trueであれば，経路をprintする

        Returns:
            Tuple[List["Node"], int, float]: 左から目的までの交換操作回数，全体交換操作回数，探索にかかった時間
        """

        start_time = time.time()
        self.reset()
        node = self.initial_node
        dist = {}
        dist[self.initial_bucket_collection.get_ball_state] = node
        q: deque = deque()
        q.append(node)

        search_count = 0
        end_node = None
        while end_node is None and q:
            search_count += 1
            node = q.popleft()
            for i in range(self.bucket_num - 1):
                for j in range(2):
                    for k in range(2):
                        next_bucket_collection = node.bucket_collection.swap(bucket_left=i, ball_in_left_bucket=j, ball_in_right_bucket=k)
                        next_node = Node(bucket_collection=next_bucket_collection, pre_node=node)
                        if self.is_goal(next_bucket_collection):
                            end_node = next_node
                            break
                        if next_bucket_collection.get_ball_state in dist:
                            continue
                        dist[next_bucket_collection.get_ball_state] = next_node
                        q.append(next_node)

        print("search end.")
        process_time = time.time() - start_time

        nodes: List[Node] = []
        if end_node is None:
            print("no answer.")
            return nodes, search_count, process_time

        node = end_node
        while node.pre_node is not None:
            nodes.append(node)
            node = node.pre_node
        nodes.reverse()
        if do_print:
            self.initial_node.print_bucket_collection()
            for i in range(len(nodes)):
                print(nodes[i].action)
                nodes[i].print_bucket_collection()

        return nodes, search_count, process_time

    def dfs_solver(self, do_print: bool) -> Tuple[List["Node"], int, float]:
        """バケツパズルDFSで解く

        Args:
            do_print (bool): Trueであれば，経路をprintする

        Returns:
            Tuple[List["Node"], int, float]: 左から目的までの交換操作回数，全体交換操作回数，探索にかかった時間
        """

        start_time = time.time()
        self.reset()
        node = self.initial_node
        dist = {}
        dist[self.initial_bucket_collection.get_ball_state] = node
        q: deque = deque()
        q.append(node)

        search_count = 0
        end_node = None
        while end_node is None and q:
            search_count += 1
            node = q.pop()
            for i in range(self.bucket_num - 1):
                for j in range(2):
                    for k in range(2):
                        next_bucket_collection = node.bucket_collection.swap(bucket_left=i, ball_in_left_bucket=j, ball_in_right_bucket=k)
                        next_node = Node(bucket_collection=next_bucket_collection, pre_node=node)
                        if self.is_goal(next_bucket_collection):
                            end_node = next_node
                            break
                        if next_bucket_collection.get_ball_state in dist:
                            continue
                        dist[next_bucket_collection.get_ball_state] = next_node
                        q.append(next_node)

        print("search end.")
        process_time = time.time() - start_time

        nodes: List[Node] = []
        if end_node is None:
            print("no answer.")
            return nodes, search_count, process_time

        node = end_node
        while node.pre_node is not None:
            nodes.append(node)
            node = node.pre_node
        nodes.reverse()
        if do_print:
            self.initial_node.print_bucket_collection()
            for i in range(len(nodes)):
                print(nodes[i].action)
                nodes[i].print_bucket_collection()

        return nodes, search_count, process_time

    def a_star_solver(self, do_print: bool) -> Tuple[List["Node"], int, float]:
        """バケツパズルA*で解く

        Args:
            do_print (bool): Trueであれば，経路をprintする

        Returns:
            Tuple[List["Node"], int, float]: 左から目的までの交換操作回数，全体交換操作回数，探索にかかった時間
        """

        start_time = time.time()
        self.reset()
        node = self.initial_node
        dist = {}
        dist[self.initial_bucket_collection.get_ball_state] = node
        q: List[Node] = []
        heappush(q, node)

        search_count = 0
        end_node = None
        while end_node is None and q:
            search_count += 1
            node = heappop(q)
            for i in range(self.bucket_num - 1):
                for j in range(2):
                    for k in range(2):
                        next_bucket_collection = node.bucket_collection.swap(bucket_left=i, ball_in_left_bucket=j, ball_in_right_bucket=k)
                        next_node = Node(bucket_collection=next_bucket_collection, pre_node=node)
                        if self.is_goal(next_bucket_collection):
                            end_node = next_node
                            break
                        if next_bucket_collection.get_ball_state in dist and dist[next_bucket_collection.get_ball_state] <= next_node:
                            continue
                        dist[next_bucket_collection.get_ball_state] = next_node
                        heappush(q, next_node)

        print("search end.")
        process_time = time.time() - start_time

        nodes: List[Node] = []
        if end_node is None:
            print("no answer.")
            return nodes, search_count, process_time

        node = end_node
        while node.pre_node is not None:
            nodes.append(node)
            node = node.pre_node
        nodes.reverse()
        if do_print:
            self.initial_node.print_bucket_collection()
            for i in range(len(nodes)):
                print(nodes[i].action)
                nodes[i].print_bucket_collection()

        return nodes, search_count, process_time


if __name__ == '__main__':
    # 適宜bucket_numとdo_printを変更してください
    # バケツの数
    bucket_num = 4
    # 経路を表示するか
    do_print = False

    bucket_puzzle_solver = BucketPuzzleSolver(bucket_num=bucket_num)
    # bucket_puzzle_solver.test()

    print('BFSでの解法')
    actions, search_count, process_time = bucket_puzzle_solver.bfs_solver(do_print=do_print)
    print(f'hands={len(actions)}, search_count={search_count}, process_time = {process_time}')

    print('DFSでの解法')
    actions, search_count, process_time = bucket_puzzle_solver.dfs_solver(do_print=do_print)
    print(f'hands={len(actions)}, search_count={search_count}, process_time = {process_time}')

    print('A*での解法')
    actions, search_count, process_time = bucket_puzzle_solver.a_star_solver(do_print=do_print)
    print(f'hands={len(actions)}, search_count={search_count}, process_time = {process_time}')
