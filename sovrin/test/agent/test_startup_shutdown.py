from plenum.common.startable import Status
from pytest import fixture

from sovrin.agent.agent import Agent


@fixture(scope="module")
def agent(tdir):
    return Agent('agent1', tdir)


@fixture(scope="module")
def startedAgent(emptyLooper, agent):
    emptyLooper.add(agent)
    return agent


def testStartup(startedAgent, emptyLooper):
    assert startedAgent.isGoing() is True
    assert startedAgent.get_status() is Status.starting
    emptyLooper.runFor(.1)
    assert startedAgent.get_status() is Status.started


def testShutdown(startedAgent):
    startedAgent.stop()
    assert startedAgent.isGoing() is False
    assert startedAgent.get_status() is Status.stopped
