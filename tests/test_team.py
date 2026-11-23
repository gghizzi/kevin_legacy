def test_team_after_kevin():
    before = Team()
    after = Kevin.join(before)

    assert after.confidence > before.confidence
    assert after.capability > before.capability
    assert after.bad_jokes > before.bad_jokes
