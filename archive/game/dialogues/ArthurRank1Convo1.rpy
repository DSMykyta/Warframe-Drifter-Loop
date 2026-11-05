# game/dialogues/ArthurRank1Convo1.rpy
label ArthurRank1Convo1:

    show arthur at char_center
    $ store.talked_today.add("Артур")


    # Node 546: StartDialogueNode
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1839']]":  # "Що змусило тебе стати солдатом?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1839']]"
            jump node_547

        "[ArthurRomance['Choice_ArthurRank1Convo1_1840']]":  # "Яким було ваше дитинство? Твоє й Елеонори?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1840']]"
            jump node_548

        "[ArthurRomance['Choice_ArthurRank1Convo1_1841']]":  # "Розкажи мені про себе."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1841']]"
            jump node_549

# Node 547: PlayerChoiceDialogueNode
label node_547:
    $ flags["ArthurSoldier"] = True
    jump node_550

# Node 548: PlayerChoiceDialogueNode
label node_548:
    $ flags["ArthurFamily"] = True
    jump node_552

# Node 549: PlayerChoiceDialogueNode
label node_549:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1843']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1842']]":  # "Ага. А воно хіба не так працює?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1842']]"
            jump node_551

        "[ArthurRomance['Choice_ArthurRank1Convo1_1844']]":  # "А що не так?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1844']]"
            jump node_554

        "[ArthurRomance['Choice_ArthurRank1Convo1_1846']]":  # "Гаразд, не звертай уваги. [Кінець]"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1846']]"
            jump node_556

# Node 550: SetBooleanDialogueNode
label node_550:
    jump node_555

# Node 551: PlayerChoiceDialogueNode
label node_551:
    jump node_558

# Node 552: SetBooleanDialogueNode
label node_552:
    jump node_555

# Node 553: DialogueNode
label node_553:
    jump node_549  # Loop back to node_549 for consistency

# Node 554: PlayerChoiceDialogueNode
label node_554:
    jump node_558

# Node 555: DialogueNode
label node_555:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1845']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_2165']]":  # "О-о, ну гаразд. Не зважай. [Кінець]"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_2165']]"
            jump node_561

        "[ArthurRomance['Choice_ArthurRank1Convo1_1850']]":  # "Ой. Ніжна тема?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1850']]"
            jump node_562

        "[ArthurRomance['Choice_ArthurRank1Convo1_1851']]":  # "Зажди. Що?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1851']]"
            jump node_563

# Node 556: PlayerChoiceDialogueNode
label node_556:
    jump node_557

# Node 558: DialogueNode
label node_558:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1847']]"
    $ advance_time(5)
    jump node_559

# Node 559: DialogueNode
label node_559:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1848']]"
    $ advance_time(5)
    jump node_570

# Node 560: DialogueNode
label node_560:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1849']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1857']]":  # "То як я це маю зробити?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1857']]"
            jump node_571

        "[ArthurRomance['Choice_ArthurRank1Convo1_1858']]":  # "То мені припинити просто зараз чи?.."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1858']]"
            jump node_572

# Node 561: PlayerChoiceDialogueNode
label node_561:
    jump node_557

# Node 562: PlayerChoiceDialogueNode
label node_562:
    jump node_565

# Node 563: PlayerChoiceDialogueNode
label node_563:
    jump node_565

# Node 565: DialogueNode
label node_565:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1852']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1853']]":  # "Ні, напевно ні."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1853']]"
            jump node_566

        "[ArthurRomance['Choice_ArthurRank1Convo1_1854']]":  # "Мені шкода."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1854']]"
            $ add_chemistry("Артур", 4)
            jump node_567

# Node 566: PlayerChoiceDialogueNode
label node_566:
    jump node_568

# Node 567: PlayerChoiceDialogueNode
label node_567:
    jump node_568

# Node 568: PlayerChoiceDialogueNode
label node_568:
    jump node_569

# Node 569: DialogueNode
label node_569:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1856']]"
    $ advance_time(5)
    jump node_576

# Node 570: ChemistryDialogueNode
label node_570:
    $ add_chemistry("Артур", 4)
    jump node_560

# Node 571: PlayerChoiceDialogueNode
label node_571:
    jump node_575

# Node 572: PlayerChoiceDialogueNode
label node_572:
    jump node_573

# Node 573: DialogueNode
label node_573:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1859']]"
    $ advance_time(5)
    jump node_574

# Node 574: DialogueNode
label node_574:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1860']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1867']]":  # "Ем… який улюблений колір?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1867']]"
            jump node_584

        "[ArthurRomance['Choice_ArthurRank1Convo1_1869']]":  # "Ем… середнє ім’я."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1869']]"
            jump node_587

        "[ArthurRomance['Choice_ArthurRank1Convo1_1870']]":  # "Перший улюбленець."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1870']]"
            jump node_588

# Node 575: DialogueNode
label node_575:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1861']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1867']]":  # "Ем… який улюблений колір?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1867']]"
            jump node_584

        "[ArthurRomance['Choice_ArthurRank1Convo1_1869']]":  # "Ем… середнє ім’я."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1869']]"
            jump node_587

        "[ArthurRomance['Choice_ArthurRank1Convo1_1870']]":  # "Перший улюбленець."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1870']]"
            jump node_588

# Node 576: DialogueNode
label node_576:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1862']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1863']]":  # "Спершу напої. *Потім* особисті питання. Ясненько."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1863']]"
            jump node_577

        "[ArthurRomance['Choice_ArthurRank1Convo1_1864']]":  # "Не вартує клопотів, не зважай. [Кінець]"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1864']]"
            jump node_578

# Node 577: PlayerChoiceDialogueNode
label node_577:
    $ add_chemistry("Артур", 4)
    jump node_579

# Node 578: PlayerChoiceDialogueNode
label node_578:
    jump node_582

# Node 579: ChemistryDialogueNode
label node_579:
    jump node_580

# Node 580: DialogueNode
label node_580:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1865']]"
    $ advance_time(5)
    jump node_557

# Node 582: DialogueNode
label node_582:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1866']]"
    $ advance_time(5)
    jump node_557

# Node 584: PlayerChoiceDialogueNode
label node_584:
    $ flags["ArthurFavoriteColor"] = True
    jump node_585

# Node 585: SetBooleanDialogueNode
label node_585:
    jump node_586

# Node 586: DialogueNode
label node_586:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1868']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1872']]":  # "Чорний."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1872']]"
            jump node_592

        "[ArthurRomance['Choice_ArthurRank1Convo1_1873']]":  # "Зелений."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1873']]"
            jump node_593

        "[ArthurRomance['Choice_ArthurRank1Convo1_1874']]":  # "Синій."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1874']]"
            jump node_594

        "[ArthurRomance['Choice_ArthurRank1Convo1_1875']]":  # "Червоний."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1875']]"
            jump node_595

# Node 587: PlayerChoiceDialogueNode
label node_587:
    $ flags["ArthurMiddleName"] = True
    jump node_589

# Node 588: PlayerChoiceDialogueNode
label node_588:
    $ flags["ArthurFirstPet"] = True
    jump node_590

# Node 589: SetBooleanDialogueNode
label node_589:
    jump node_591

# Node 590: SetBooleanDialogueNode
label node_590:
    jump node_2777

# Node 591: DialogueNode
label node_591:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1871']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1899']]":  # "Брекстон"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1899']]"
            jump node_627

        "[ArthurRomance['Choice_ArthurRank1Convo1_1900']]":  # "Герберт"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1900']]"
            jump node_628

        "[ArthurRomance['Choice_ArthurRank1Convo1_1901']]":  # "Джеймс"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1901']]"
            jump node_629

        "[ArthurRomance['Choice_ArthurRank1Convo1_1902']]":  # "Пітерсгем"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1902']]"
            jump node_635

# Node 592: PlayerChoiceDialogueNode
label node_592:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1876']]"
    $ advance_time(5)
    jump node_602

# Node 593: PlayerChoiceDialogueNode
label node_593:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1877']]"
    $ advance_time(5)
    jump node_618

# Node 594: PlayerChoiceDialogueNode
label node_594:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1878']]"
    $ advance_time(5)
    jump node_618

# Node 595: PlayerChoiceDialogueNode
label node_595:
    $ add_chemistry("Артур", 4)
    jump node_601

# Node 599: DialogueNode
label node_599:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1879']]"
    $ advance_time(5)
    jump node_600

# Node 600: SetBooleanDialogueNode
label node_600:
    $ flags["ArthurFavoriteColorRed"] = True
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1892']]":  # "Бандана на твоїй скані."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1892']]"
            jump node_619

        "[ArthurRomance['Choice_ArthurRank1Convo1_1893']]":  # "За «відчуттями» ти з червоних."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1893']]"
            jump node_620

# Node 601: ChemistryDialogueNode
label node_601:
    jump node_599

# Node 602: DialogueNode
label node_602:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1880']]"
    $ advance_time(5)
    jump node_603

# Node 603: DialogueNode
label node_603:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1881']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1882']]":  # "Узагалі-то я не знаю таких подробиць про вас двох."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1882']]"
            jump node_604

        "[ArthurRomance['Choice_ArthurRank1Convo1_1883']]":  # "Хай там як, але чорний навіть не колір. [Кінець]"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1883']]"
            jump node_605

# Node 604: PlayerChoiceDialogueNode
label node_604:
    jump node_608

# Node 605: PlayerChoiceDialogueNode
label node_605:
    jump node_606

# Node 606: DialogueNode
label node_606:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1884']]"
    $ advance_time(5)
    jump node_557

# Node 608: DialogueNode
label node_608:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1885']]"
    $ advance_time(5)
    jump node_609

# Node 609: DialogueNode
label node_609:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1886']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1887']]":  # "Мені хотілося би змінити це."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1887']]"
            jump node_610

        "[ArthurRomance['Choice_ArthurRank1Convo1_1888']]":  # "З таким ставленням і не дізнаєшся. [Кінець]"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1888']]"
            jump node_611

# Node 610: PlayerChoiceDialogueNode
label node_610:
    $ flags["ArthurFamily"] = True
    jump node_615

# Node 611: PlayerChoiceDialogueNode
label node_611:
    jump node_612

# Node 612: DialogueNode
label node_612:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1889']]"
    $ advance_time(5)
    jump node_557

# Node 614: ChemistryDialogueNode
label node_614:
    $ add_chemistry("Артур", 4)
    jump node_616

# Node 615: SetBooleanDialogueNode
label node_615:
    jump node_614

# Node 616: DialogueNode
label node_616:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1890']]"
    $ advance_time(5)
    jump node_557

# Node 618: DialogueNode
label node_618:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1891']]"
    $ advance_time(5)
    jump node_625

# Node 619: PlayerChoiceDialogueNode
label node_619:
    jump node_621

# Node 620: PlayerChoiceDialogueNode
label node_620:
    jump node_626

# Node 621: DialogueNode
label node_621:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1894']]"
    $ advance_time(5)
    jump node_623

# Node 622: DialogueNode
label node_622:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1895']]"
    $ advance_time(5)
    jump node_624

# Node 623: PlayerChoiceDialogueNode
label node_623:
    jump node_622

# Node 624: SetBooleanDialogueNode
label node_624:
    $ flags["ArthurSkana"] = True
    jump node_625

# Node 625: DialogueNode
label node_625:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1897']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1924']]":  # "Так. Скажімо, на зараз досить."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1924']]"
            jump node_657

        "[ArthurRomance['Choice_ArthurRank1Convo1_1925']]":  # "Звичайно, якщо ти більше нічим не хочеш поділитися."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1925']]"
            jump node_658

# Node 626: DialogueNode
label node_626:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1898']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1926']]":  # "А де і як ви жили? Ну, до цього всього?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1926']]"
            jump node_659

        "[ArthurRomance['Choice_ArthurRank1Convo1_1927']]":  # "Навчаюся у найкмітливіших. ;)"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1927']]"
            jump node_660

# Node 627: PlayerChoiceDialogueNode
label node_627:
    jump node_631

# Node 628: PlayerChoiceDialogueNode
label node_628:
    jump node_632

# Node 629: PlayerChoiceDialogueNode
label node_629:
    $ add_chemistry("Артур", 4)
    jump node_637

# Node 631: DialogueNode
label node_631:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1903']]"
    $ advance_time(5)
    jump node_639

# Node 632: DialogueNode
label node_632:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1904']]"
    $ advance_time(5)
    jump node_640

# Node 633: DialogueNode
label node_633:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1905']]"
    $ advance_time(5)
    jump node_634

# Node 634: DialogueNode
label node_634:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1906']]"
    $ advance_time(5)
    jump node_638

# Node 635: SetBooleanDialogueNode
label node_635:
    $ flags["ArthurMiddleNamePetersham"] = True
    jump node_636

# Node 636: DialogueNode
label node_636:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1907']]"
    $ advance_time(5)
    jump node_647

# Node 637: ChemistryDialogueNode
label node_637:
    jump node_633

# Node 638: SetBooleanDialogueNode
label node_638:
    $ flags["ArthurMiddleNameJames"] = True
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1908']]":  # "Це просто випадкова здогадка."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1908']]"
            jump node_645

        "[ArthurRomance['Choice_ArthurRank1Convo1_1909']]":  # "Ти «відчуваєшся» як Джеймс."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1909']]"
            jump node_646

# Node 639: DialogueNode
label node_639:
    jump node_640

# Node 640: DialogueNode
label node_640:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1919']]"
    $ advance_time(5)
    jump node_641

# Node 641: DialogueNode
label node_641:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1920']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1921']]":  # "Як мило."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1921']]"
            jump node_642

        "[ArthurRomance['Choice_ArthurRank1Convo1_1922']]":  # "Нудне."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1922']]"
            jump node_643

# Node 642: PlayerChoiceDialogueNode
label node_642:
    jump node_644

# Node 643: PlayerChoiceDialogueNode
label node_643:
    jump node_644

# Node 644: DialogueNode
label node_644:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1923']]"
    $ advance_time(5)
    jump node_625

# Node 645: PlayerChoiceDialogueNode
label node_645:
    jump node_625

# Node 646: PlayerChoiceDialogueNode
label node_646:
    jump node_626

# Node 647: DialogueNode
label node_647:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1910']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1911']]":  # "Мені шкода, що я не знаю оновленого списку британських імен 20 століття!"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1911']]"
            jump node_648

        "[ArthurRomance['Choice_ArthurRank1Convo1_1912']]":  # "А мені звідкіля це знати?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1912']]"
            jump node_649

# Node 648: PlayerChoiceDialogueNode
label node_648:
    jump node_650

# Node 649: PlayerChoiceDialogueNode
label node_649:
    jump node_650

# Node 650: DialogueNode
label node_650:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1913']]"
    $ advance_time(5)
    jump node_651

# Node 651: DialogueNode
label node_651:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1914']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1915']]":  # "Обережніше, бо почну так називати весь час."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1915']]"
            jump node_652

        "[ArthurRomance['Choice_ArthurRank1Convo1_1916']]":  # "Так-так. Смійся на здоров’я."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1916']]"
            jump node_653

# Node 652: PlayerChoiceDialogueNode
label node_652:
    $ add_chemistry("Артур", 4)
    jump node_655

# Node 653: PlayerChoiceDialogueNode
label node_653:
    jump node_655

# Node 654: DialogueNode
label node_654:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1917']]"
    $ advance_time(5)
    jump node_656

# Node 655: ChemistryDialogueNode
label node_655:
    jump node_557

# Node 656: DialogueNode
label node_656:
    jump node_657

# Node 657: PlayerChoiceDialogueNode
label node_657:
    jump node_663

# Node 658: PlayerChoiceDialogueNode
label node_658:
    jump node_667

# Node 659: PlayerChoiceDialogueNode
label node_659:
    $ flags["ArthurFamily"] = True
    jump node_666

# Node 660: PlayerChoiceDialogueNode
label node_660:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1928']]"
    $ advance_time(5)
    jump node_661

# Node 661: DialogueNode
label node_661:
    jump node_557

# Node 663: DialogueNode
label node_663:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1929']]"
    $ advance_time(5)
    jump node_557

# Node 665: PlayerChoiceDialogueNode
label node_665:
    jump node_675

# Node 666: SetBooleanDialogueNode
label node_666:
    jump node_667

# Node 667: CheckBooleanDialogueNode
label node_667:
    if flags.get("ArthurFavoriteColor", False):
        jump node_670
    jump node_668

# Node 668: CheckBooleanDialogueNode
label node_668:
    if flags.get("ArthurMiddleName", False):
        jump node_671
    jump node_669

# Node 669: CheckBooleanDialogueNode
label node_669:
    if flags.get("ArthurFirstPet", False):
        jump node_672
    jump node_673

# Node 670: DialogueNode
label node_670:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1931']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1930']]":  # "Зарано питаю?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1930']]"
            jump node_665

        "[ArthurRomance['Choice_ArthurRank1Convo1_1935']]":  # "Вартувало спробувати."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1935']]"
            jump node_674

# Node 671: DialogueNode
label node_671:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1932']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1930']]":  # "Зарано питаю?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1930']]"
            jump node_665

        "[ArthurRomance['Choice_ArthurRank1Convo1_1935']]":  # "Вартувало спробувати."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1935']]"
            jump node_674

# Node 672: DialogueNode
label node_672:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1933']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1930']]":  # "Зарано питаю?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1930']]"
            jump node_665

        "[ArthurRomance['Choice_ArthurRank1Convo1_1935']]":  # "Вартувало спробувати."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1935']]"
            jump node_674

# Node 673: DialogueNode
label node_673:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1934']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_1930']]":  # "Зарано питаю?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1930']]"
            jump node_665

        "[ArthurRomance['Choice_ArthurRank1Convo1_1935']]":  # "Вартувало спробувати."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_1935']]"
            jump node_674

# Node 674: PlayerChoiceDialogueNode
label node_674:
    jump node_676

# Node 675: DialogueNode
label node_675:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1936']]"
    $ advance_time(5)
    jump node_677

# Node 676: DialogueNode
label node_676:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_1937']]"
    $ advance_time(5)
    jump node_557

# Node 677: DialogueNode
label node_677:
    jump node_678

# Node 678: DialogueNode
label node_678:
    jump node_557

# Node 2777: DialogueNode
label node_2777:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_3643']]"
    $ advance_time(5)
    jump node_2778

# Node 2778: DialogueNode
label node_2778:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_3644']]"
    $ advance_time(5)
    jump node_2779

# Node 2779: DialogueNode
label node_2779:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_3645']]"
    $ advance_time(5)
    jump node_2780

# Node 2780: DialogueNode
label node_2780:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_3646']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_3647']]":  # "Гадаю, що ти усунув проблеми з водою?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_3647']]"
            jump node_2781

        "[ArthurRomance['Choice_ArthurRank1Convo1_3648']]":  # "Ого. Як мило."
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_3648']]"
            jump node_2782

# Node 2781: PlayerChoiceDialogueNode
label node_2781:
    jump node_2783

# Node 2782: PlayerChoiceDialogueNode
label node_2782:
    jump node_2784

# Node 2783: DialogueNode
label node_2783:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_3649']]"
    $ advance_time(5)
    jump node_625

# Node 2784: DialogueNode
label node_2784:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_3650']]"
    $ advance_time(5)
    menu:
        "[ArthurRomance['Choice_ArthurRank1Convo1_3652']]":  # "Га? Чому ні?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_3652']]"
            jump node_2020

        "[ArthurRomance['Choice_ArthurRank1Convo1_3653']]":  # "І як ти почувався?"
            $ advance_time(5)
            mc "[ArthurRomance['Choice_ArthurRank1Convo1_3653']]"
            jump node_2409

# Node 2020: PlayerChoiceDialogueNode
label node_2020:
    jump node_2785

# Node 2409: PlayerChoiceDialogueNode
label node_2409:
    jump node_626

# Node 2785: DialogueNode
label node_2785:
    ar "[ArthurRomance['TxtArthur_ArthurRank1Convo1_3651']]"
    $ advance_time(5)
    jump node_625

# Node 557: EndDialogueNode
label node_557:
    $ store.seen_dialogues.add("arthur_rank1_deep")
    $ set_flag("arthur_rank1_deep_done")
    hide arthur
    window hide
    return
