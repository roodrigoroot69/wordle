from mamba import describe, context, it
from expects import expect, raise_error, be_true, be_false
from wordle.infra.repositories.winners_repository import PostgresWinnerRepository
from sqlalchemy.orm import Session
from unittest.mock import Mock


with describe('PostgresWinnerRepository'):

    with context('save_winner'):
        with it('saves a winner'):
            mock_db_session = Mock(spec=Session)
            repository = PostgresWinnerRepository(db=mock_db_session)

            user_id = 1
            word = "atole"

            repository.save_winner(user_id, word)

            expect(mock_db_session.add.called).to(be_true)
            expect(mock_db_session.commit.called).to(be_true)
            expect(mock_db_session.refresh.called).to(be_true)

