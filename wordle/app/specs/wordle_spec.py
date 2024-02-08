from mamba import describe, context, it, before
from expects import equal, expect, raise_error
from unittest.mock import Mock, create_autospec, call

from fastapi import HTTPException

from wordle.app.wordle_play import WordlePlayProcessor
from common.infra.models import User

with describe(WordlePlayProcessor) as self:

    with before.all:
        self.user_record = create_autospec(spec=User)
        self.user_record.word = 'verde'
        self.word_repository_mock = Mock()
        self.cache_repository_mock = Mock()
        self.use_case = WordlePlayProcessor(
            word_repository=self.word_repository_mock,
            word='cafes',
            cache_repository=self.cache_repository_mock,
            user={'username':'rodrigo'},
        )

    with context('when the user make their first attempt and guess a letter right'):
        with it('should return the correct letter with 2 value and other with 3 value and add try'):
            self.word_repository_mock.get_active_word.return_value = self.user_record
            self.cache_repository_mock.get_attempt.return_value = 1

            result = self.use_case.execute()

            expect(result).to(equal([{'letter': 'c', 'value': 3},
                                     {'letter': 'a', 'value': 3},
                                     {'letter': 'f', 'value': 3},
                                     {'letter': 'e', 'value': 2},
                                     {'letter': 's', 'value': 3}]))
            expect(self.cache_repository_mock.save_attempt.call_args).to(
                equal(
                    call(
                        'rodrigo',
                        2
                    )
                )
            )

    with context('when the user make their first attempt and guess a letter right and the right position'):
        with it('should return the correct letter with 1 value and other with 3 value and add try'):
            self.word_repository_mock.get_active_word.return_value = self.user_record
            self.cache_repository_mock.get_attempt.return_value = 1
            use_case = WordlePlayProcessor(
            word_repository=self.word_repository_mock,
            word='atole',
            cache_repository=self.cache_repository_mock,
            user={'username':'rodrigo'},
        )

            result = use_case.execute()

            expect(result).to(equal([{'letter': 'a', 'value': 3},
                                     {'letter': 't', 'value': 3},
                                     {'letter': 'o', 'value': 3},
                                     {'letter': 'l', 'value': 3},
                                     {'letter': 'e', 'value': 1}]))
            expect(self.cache_repository_mock.save_attempt.call_args).to(
                equal(
                    call(
                        'rodrigo',
                        2
                    )
                )
            )

    with context('when the user make their first attempt and does not get any letter right'):
        with it('should return all letters with 3 and add try'):
            self.word_repository_mock.get_active_word.return_value = self.user_record
            self.cache_repository_mock.get_attempt.return_value = 1
            use_case = WordlePlayProcessor(
            word_repository=self.word_repository_mock,
            word='jamon',
            cache_repository=self.cache_repository_mock,
            user={'username':'rodrigo'},
        )

            result = use_case.execute()

            expect(result).to(equal([{'letter': 'j', 'value': 3},
                                     {'letter': 'a', 'value': 3},
                                     {'letter': 'm', 'value': 3},
                                     {'letter': 'o', 'value': 3},
                                     {'letter': 'n', 'value': 3}]))
            expect(self.cache_repository_mock.save_attempt.call_args).to(
                equal(
                    call(
                        'rodrigo',
                        2
                    )
                )
            )

    with context('when the user exceed attempts allowed'):
        with it('should raise exception'):
            self.word_repository_mock.get_active_word.return_value = self.user_record
            self.cache_repository_mock.get_attempt.return_value = 6
            use_case = WordlePlayProcessor(
            word_repository=self.word_repository_mock,
            word='jamon',
            cache_repository=self.cache_repository_mock,
            user={'username':'rodrigo'},
        )

            expect(lambda: use_case.execute()).to(raise_error(HTTPException))



    with context('when the user send a word different from 5 letters'):
        with it('should raise exception'):
            self.word_repository_mock.get_active_word.return_value = self.user_record
            self.cache_repository_mock.get_attempt.return_value = 6
            use_case = WordlePlayProcessor(
            word_repository=self.word_repository_mock,
            word='venustiano',
            cache_repository=self.cache_repository_mock,
            user={'username':'rodrigo'},
        )

            expect(lambda: use_case.execute()).to(raise_error(HTTPException))
