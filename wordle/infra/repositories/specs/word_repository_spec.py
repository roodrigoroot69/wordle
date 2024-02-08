from mamba import describe, context, it
from expects import expect, have_property, be_true
from wordle.infra.repositories.word_repository import PostgresWordRepository
from sqlalchemy.orm import Session
from unittest.mock import Mock


with describe('PostgresWordRepository'):

    with context('get_active_word'):
        with it('returns an active word'):
            mock_db_session = Mock(spec=Session)
            repository = PostgresWordRepository(db=mock_db_session)

            mock_db_session.query().filter().first.return_value = Mock()

            active_word = repository.get_active_word()

            expect(active_word).to(have_property('word'))
            expect(mock_db_session.query.called).to(be_true)
            expect(mock_db_session.query().filter().first.called).to(be_true)
