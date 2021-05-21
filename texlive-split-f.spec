%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-f
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1436:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/custom-bib.tar.xz
Source1437:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/custom-bib.doc.tar.xz
Source1534:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctan_chk.doc.tar.xz
Source1758:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cryst.tar.xz
Source1759:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cryst.doc.tar.xz
Source1760:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyklop.tar.xz
Source1761:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyklop.doc.tar.xz
Source1762:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dancers.tar.xz
Source1763:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dantelogo.tar.xz
Source1764:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dantelogo.doc.tar.xz
Source1765:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dejavu.tar.xz
Source1766:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dejavu.doc.tar.xz
Source2206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crossword.tar.xz
Source2207:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crossword.doc.tar.xz
Source2209:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crosswrd.tar.xz
Source2210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crosswrd.doc.tar.xz
Source2263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/c-pascal.tar.xz
Source2264:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/c-pascal.doc.tar.xz
Source2493:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dad.tar.xz
Source2494:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dad.doc.tar.xz
Source2514:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctex.tar.xz
Source2515:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctex.doc.tar.xz
Source2517:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctex-faq.doc.tar.xz
Source2541:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyrplain.tar.xz
Source2593:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cs.tar.xz
Source2594:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/csbulletin.tar.xz
Source2595:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/csbulletin.doc.tar.xz
Source2599:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cstex.doc.tar.xz
Source2741:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/csquotes-de.doc.tar.xz
Source2742:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dehyph-exptl.tar.xz
Source2743:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dehyph-exptl.doc.tar.xz
Source2932:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctib.tar.xz
Source2933:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctib.doc.tar.xz
Source2975:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cursolatex.doc.tar.xz
Source2996:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crop.tar.xz
Source2997:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crop.doc.tar.xz
Source2999:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctable.tar.xz
Source3000:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctable.doc.tar.xz
Source3111:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/curve.tar.xz
Source3112:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/curve.doc.tar.xz
Source3114:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/curve2e.tar.xz
Source3115:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/curve2e.doc.tar.xz
Source3117:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/curves.tar.xz
Source3118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/curves.doc.tar.xz
Source3120:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dcpic.tar.xz
Source3121:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dcpic.doc.tar.xz
Source3483:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cprotect.tar.xz
Source3484:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cprotect.doc.tar.xz
Source3486:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crbox.tar.xz
Source3487:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crbox.doc.tar.xz
Source3488:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crossreference.tar.xz
Source3489:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crossreference.doc.tar.xz
Source3491:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/csquotes.tar.xz
Source3492:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/csquotes.doc.tar.xz
Source3493:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/csvsimple.tar.xz
Source3494:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/csvsimple.doc.tar.xz
Source3495:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cuisine.tar.xz
Source3496:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cuisine.doc.tar.xz
Source3498:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/currfile.tar.xz
Source3499:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/currfile.doc.tar.xz
Source3501:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/currvita.tar.xz
Source3502:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/currvita.doc.tar.xz
Source3504:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cutwin.tar.xz
Source3505:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cutwin.doc.tar.xz
Source3507:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cv.tar.xz
Source3508:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cv.doc.tar.xz
Source3509:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cv4tw.tar.xz
Source3510:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cv4tw.doc.tar.xz
Source3511:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cweb-latex.tar.xz
Source3512:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cweb-latex.doc.tar.xz
Source3513:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyber.tar.xz
Source3514:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyber.doc.tar.xz
Source3516:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cybercic.tar.xz
Source3517:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cybercic.doc.tar.xz
Source3519:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dashbox.tar.xz
Source3520:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dashbox.doc.tar.xz
Source3522:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dashrule.tar.xz
Source3523:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dashrule.doc.tar.xz
Source3525:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dashundergaps.tar.xz
Source3526:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dashundergaps.doc.tar.xz
Source3527:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dataref.tar.xz
Source3528:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dataref.doc.tar.xz
Source3530:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datatool.tar.xz
Source3531:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datatool.doc.tar.xz
Source3533:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dateiliste.tar.xz
Source3534:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dateiliste.doc.tar.xz
Source3536:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datenumber.tar.xz
Source3537:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datenumber.doc.tar.xz
Source3539:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime.tar.xz
Source3540:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime.doc.tar.xz
Source3542:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2.tar.xz
Source3543:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2.doc.tar.xz
Source3545:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-bahasai.tar.xz
Source3546:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-bahasai.doc.tar.xz
Source3548:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-basque.tar.xz
Source3549:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-basque.doc.tar.xz
Source3551:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-breton.tar.xz
Source3552:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-breton.doc.tar.xz
Source3554:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-bulgarian.tar.xz
Source3555:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-bulgarian.doc.tar.xz
Source3557:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-catalan.tar.xz
Source3558:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-catalan.doc.tar.xz
Source3560:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-croatian.tar.xz
Source3561:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-croatian.doc.tar.xz
Source3563:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-czech.tar.xz
Source3564:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-czech.doc.tar.xz
Source3566:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-danish.tar.xz
Source3567:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-danish.doc.tar.xz
Source3569:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-dutch.tar.xz
Source3570:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-dutch.doc.tar.xz
Source3572:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-en-fulltext.tar.xz
Source3573:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-en-fulltext.doc.tar.xz
Source3575:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-english.tar.xz
Source3576:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-english.doc.tar.xz
Source3578:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-esperanto.tar.xz
Source3579:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-esperanto.doc.tar.xz
Source3581:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-estonian.tar.xz
Source3582:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-estonian.doc.tar.xz
Source3584:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-finnish.tar.xz
Source3585:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-finnish.doc.tar.xz
Source3587:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-french.tar.xz
Source3588:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-french.doc.tar.xz
Source3590:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-galician.tar.xz
Source3591:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-galician.doc.tar.xz
Source3593:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-german.tar.xz
Source3594:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-german.doc.tar.xz
Source3596:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-greek.tar.xz
Source3597:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-greek.doc.tar.xz
Source3599:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-hebrew.tar.xz
Source3600:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-hebrew.doc.tar.xz
Source3602:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-icelandic.tar.xz
Source3603:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-icelandic.doc.tar.xz
Source3605:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-irish.tar.xz
Source3606:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-irish.doc.tar.xz
Source3608:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-italian.tar.xz
Source3609:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-italian.doc.tar.xz
Source3611:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-it-fulltext.tar.xz
Source3612:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-it-fulltext.doc.tar.xz
Source3614:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-latin.tar.xz
Source3615:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-latin.doc.tar.xz
Source3617:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-lsorbian.tar.xz
Source3618:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-lsorbian.doc.tar.xz
Source3620:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-magyar.tar.xz
Source3621:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-magyar.doc.tar.xz
Source3623:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-norsk.tar.xz
Source3624:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-norsk.doc.tar.xz
Source3626:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-polish.tar.xz
Source3627:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-polish.doc.tar.xz
Source3629:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-portuges.tar.xz
Source3630:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-portuges.doc.tar.xz
Source3632:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-romanian.tar.xz
Source3633:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-romanian.doc.tar.xz
Source3635:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-russian.tar.xz
Source3636:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-russian.doc.tar.xz
Source3638:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-samin.tar.xz
Source3639:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-samin.doc.tar.xz
Source3641:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-scottish.tar.xz
Source3642:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-scottish.doc.tar.xz
Source3644:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-serbian.tar.xz
Source3645:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-serbian.doc.tar.xz
Source3647:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-slovak.tar.xz
Source3648:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-slovak.doc.tar.xz
Source3650:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-slovene.tar.xz
Source3651:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-slovene.doc.tar.xz
Source3653:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-spanish.tar.xz
Source3654:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-spanish.doc.tar.xz
Source3656:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-swedish.tar.xz
Source3657:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-swedish.doc.tar.xz
Source3659:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-turkish.tar.xz
Source3660:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-turkish.doc.tar.xz
Source3662:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-ukrainian.tar.xz
Source3663:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-ukrainian.doc.tar.xz
Source3665:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-usorbian.tar.xz
Source3666:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-usorbian.doc.tar.xz
Source3668:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-welsh.tar.xz
Source3669:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/datetime2-welsh.doc.tar.xz
Source3671:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dblfloatfix.tar.xz
Source3672:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dblfloatfix.doc.tar.xz
Source3673:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/decimal.tar.xz
Source3674:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/decimal.doc.tar.xz
Source3676:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/decorule.tar.xz
Source3677:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/decorule.doc.tar.xz
Source3679:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/delim.tar.xz
Source3680:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/delim.doc.tar.xz
Source3682:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/delimtxt.tar.xz
Source3683:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/delimtxt.doc.tar.xz
Source3685:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/denisbdoc.tar.xz
Source3686:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/denisbdoc.doc.tar.xz
Source6345:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dccpaper.tar.xz
Source6346:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dccpaper.doc.tar.xz
Source6645:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cryptocode.tar.xz
Source6646:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cryptocode.doc.tar.xz
Source7299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cquthesis.tar.xz
Source7300:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cquthesis.doc.tar.xz
Source7302:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crimson.tar.xz
Source7303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crimson.doc.tar.xz
Source7304:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctablestack.tar.xz
Source7305:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctablestack.doc.tar.xz
Source7307:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/delimseasy.tar.xz
Source7308:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/delimseasy.doc.tar.xz
Source7712:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crossreftools.tar.xz
Source7713:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crossreftools.doc.tar.xz
Source7714:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/css-colors.tar.xz
Source7715:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/css-colors.doc.tar.xz
Source7716:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cstypo.tar.xz
Source7717:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cstypo.doc.tar.xz
Source7718:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/currency.tar.xz
Source7719:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/currency.doc.tar.xz
Source8114:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cqubeamer.tar.xz
Source8115:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cqubeamer.doc.tar.xz
Source8118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dejavu-otf.tar.xz
Source8119:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dejavu-otf.doc.tar.xz
Source8120:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/delimset.tar.xz
Source8121:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/delimset.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-custom-bib
Provides:       tex-custom-bib = %{tl_version}
License:        LPPL
Summary:        Customised BibTeX styles
Version:        svn24729.4.33

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(geophys.tex) = %{tl_version}, tex(makebst.tex) = %{tl_version}
Provides:       tex(shorthnd.tex) = %{tl_version}

%description -n texlive-custom-bib
Package generating customized BibTeX bibliography styles from a
generic file using docstrip driven by parameters generated by a
menu application. Includes support for the Harvard style of
citations.

%package -n texlive-custom-bib-doc
Summary:        Documentation for custom-bib
Version:        svn24729.4.33

Provides:       tex-custom-bib-doc
AutoReqProv:    No

%description -n texlive-custom-bib-doc
Documentation for custom-bib

%package -n texlive-ctan_chk-doc
Summary:        Documentation for ctan_chk
Version:        svn36304.1.0

Provides:       tex-ctan_chk-doc
AutoReqProv:    No

%description -n texlive-ctan_chk-doc
Documentation for ctan_chk

%package -n texlive-cryst
Provides:       tex-cryst = %{tl_version}
License:        LPPL
Summary:        Font for graphical symbols used in crystallography
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cryst.tfm) = %{tl_version}, tex(cryst.pfb) = %{tl_version}

%description -n texlive-cryst
The font is provided as an Adobe Type 1 font, and as Metafont
source. Instructions for use are available both in the README
file and (with a font diagram) in the documentation.

%package -n texlive-cryst-doc
Summary:        Documentation for cryst
Version:        svn15878.0

Provides:       tex-cryst-doc
AutoReqProv:    No

%description -n texlive-cryst-doc
Documentation for cryst

%package -n texlive-cyklop
Provides:       tex-cyklop = %{tl_version}
License:        LPPL
Summary:        The Cyclop typeface
Version:        svn18651.0.915

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(cs-cyklop-sc.enc) = %{tl_version}, tex(cs-cyklop.enc) = %{tl_version}
Provides:       tex(ec-cyklop-sc.enc) = %{tl_version}, tex(ec-cyklop.enc) = %{tl_version}
Provides:       tex(l7x-cyklop-sc.enc) = %{tl_version}, tex(l7x-cyklop.enc) = %{tl_version}
Provides:       tex(ly1-cyklop-sc.enc) = %{tl_version}, tex(ly1-cyklop.enc) = %{tl_version}
Provides:       tex(qx-cyklop-sc.enc) = %{tl_version}, tex(qx-cyklop.enc) = %{tl_version}
Provides:       tex(t5-cyklop-sc.enc) = %{tl_version}, tex(t5-cyklop.enc) = %{tl_version}
Provides:       tex(cyklop-cs.map) = %{tl_version}, tex(cyklop-ec.map) = %{tl_version}
Provides:       tex(cyklop-l7x.map) = %{tl_version}, tex(cyklop-ly1.map) = %{tl_version}
Provides:       tex(cyklop-qx.map) = %{tl_version}, tex(cyklop-t5.map) = %{tl_version}
Provides:       tex(cyklop.map) = %{tl_version}, tex(cyklop-italic.otf) = %{tl_version}
Provides:       tex(cyklop-regular.otf) = %{tl_version}, tex(cs-cyklopi-sc.tfm) = %{tl_version}
Provides:       tex(cs-cyklopi.tfm) = %{tl_version}, tex(cs-cyklopr-sc.tfm) = %{tl_version}
Provides:       tex(cs-cyklopr.tfm) = %{tl_version}, tex(ec-cyklopi-sc.tfm) = %{tl_version}
Provides:       tex(ec-cyklopi.tfm) = %{tl_version}, tex(ec-cyklopr-sc.tfm) = %{tl_version}
Provides:       tex(ec-cyklopr.tfm) = %{tl_version}, tex(l7x-cyklopi-sc.tfm) = %{tl_version}
Provides:       tex(l7x-cyklopi.tfm) = %{tl_version}, tex(l7x-cyklopr-sc.tfm) = %{tl_version}
Provides:       tex(l7x-cyklopr.tfm) = %{tl_version}, tex(ly1-cyklopi-sc.tfm) = %{tl_version}
Provides:       tex(ly1-cyklopi.tfm) = %{tl_version}, tex(ly1-cyklopr-sc.tfm) = %{tl_version}
Provides:       tex(ly1-cyklopr.tfm) = %{tl_version}, tex(qx-cyklopi-sc.tfm) = %{tl_version}
Provides:       tex(qx-cyklopi.tfm) = %{tl_version}, tex(qx-cyklopr-sc.tfm) = %{tl_version}
Provides:       tex(qx-cyklopr.tfm) = %{tl_version}, tex(t5-cyklopi-sc.tfm) = %{tl_version}
Provides:       tex(t5-cyklopi.tfm) = %{tl_version}, tex(t5-cyklopr-sc.tfm) = %{tl_version}
Provides:       tex(t5-cyklopr.tfm) = %{tl_version}, tex(cyklopi.pfb) = %{tl_version}
Provides:       tex(cyklopr.pfb) = %{tl_version}, tex(cyklop.sty) = %{tl_version}
Provides:       tex(il2cyklop.fd) = %{tl_version}, tex(l7xcyklop.fd) = %{tl_version}
Provides:       tex(ly1cyklop.fd) = %{tl_version}, tex(ot1cyklop.fd) = %{tl_version}
Provides:       tex(ot4cyklop.fd) = %{tl_version}, tex(qxcyklop.fd) = %{tl_version}
Provides:       tex(t1cyklop.fd) = %{tl_version}, tex(t5cyklop.fd) = %{tl_version}

%description -n texlive-cyklop
The Cyclop typeface was designed in the 1920s at the workshop
of Warsaw type foundry "Odlewnia Czcionek J. Idzkowski i S-ka".
This sans serif typeface has a highly modulated stroke so it
has high typographic contrast. The vertical stems are much
heavier then horizontal ones. Most characters have thin
rectangles as additional counters giving the unique shape of
the characters. The lead types of Cyclop typeface were produced
in slanted variant at sizes 8-48 pt. It was heavily used for
heads in newspapers and accidents prints. Typesetters used
Cyclop in the inter-war period, during the occupation in the
underground press. The typeface was used until the beginnings
of the offset print and computer typesetting era. Nowadays it
is hard to find the metal types of this typeface. The font was
generated using the Metatype1 package. Then the original set of
characters was completed by adding the full set of accented
letters and characters of the modern Latin alphabets (including
Vietnamese). The upright variant was generated and it was more
complicated task than it appeared at the beginning. 11 upright
letters of the Cyclop typeface were presented in the book by
Filip Trzaska, "Podstawy techniki wydawniczej" ("Foundation of
the publishing techonology"), Warsaw 1967. But even the author
of the book does not know what was the source of the presented
examples. The fonts are distributed in the Type1 and OpenType
formats along with the files necessary for use these fonts in
TeX and LaTeX including encoding definition files: T1 (ec), T5
(Vietnamese), OT4, QX, texnansi and nonstandard ones (IL2 for
Czech fonts).

%package -n texlive-cyklop-doc
Summary:        Documentation for cyklop
Version:        svn18651.0.915

Provides:       tex-cyklop-doc
AutoReqProv:    No

%description -n texlive-cyklop-doc
Documentation for cyklop

%package -n texlive-dancers
Provides:       tex-dancers = %{tl_version}
License:        Copyright only
Summary:        Font for Conan Doyle'ss "The Dancing Men"
Version:        svn13293.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dancers.tfm) = %{tl_version}

%description -n texlive-dancers
The (Sherlock Holmes) book contains a code which uses dancing
men as glyphs. The alphabet as given is not complete, lacking
f, j, k, q, u, w, x and z, so those letters in the font are not
due to Conan Doyle. The code required word endings to be marked
by the dancing man representing the last letter to be holding a
flag: these are coded as A-Z.
thaTiStOsaYsentenceSiNthEcodElooKlikEthiS. In some cases, the
man has no arms, making it impossible for him to hold a flag.
In these cases, he is wearing a flag on his hat in the
'character'. The font is distributed as Metafont source; it
works poorly in modern environments, and could do with expert
attention (if you are interested, please contact the CTAN team
for details).

%package -n texlive-dantelogo
Provides:       tex-dantelogo = %{tl_version}
License:        LPPL
Summary:        A font for DANTE's logo
Version:        svn38599

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(iftex.sty), tex(fontenc.sty), tex(fontspec.sty)
Provides:       tex(dante.enc) = %{tl_version}, tex(dante.map) = %{tl_version}
Provides:       tex(DANTE-Bold-Italic.otf) = %{tl_version}
Provides:       tex(DANTE-Bold.otf) = %{tl_version}, tex(DANTE-Italic.otf) = %{tl_version}
Provides:       tex(DANTE.otf) = %{tl_version}, tex(DANTE-Bold--texnansx--base.tfm) = %{tl_version}
Provides:       tex(DANTE-Bold--texnansx.tfm) = %{tl_version}
Provides:       tex(DANTE-Bold-Italic--texnansx--base.tfm) = %{tl_version}
Provides:       tex(DANTE-Bold-Italic--texnansx.tfm) = %{tl_version}
Provides:       tex(DANTE-Bold.tfm) = %{tl_version}, tex(DANTE-Italic--texnansx--base.tfm) = %{tl_version}
Provides:       tex(DANTE-Italic--texnansx.tfm) = %{tl_version}
Provides:       tex(DANTE.tfm) = %{tl_version}, tex(DANTE-Bold-Italic.pfb) = %{tl_version}
Provides:       tex(DANTE-Bold.pfb) = %{tl_version}, tex(DANTE-Italic.pfb) = %{tl_version}
Provides:       tex(DANTE.pfb) = %{tl_version}, tex(DANTE-Bold--texnansx.vf) = %{tl_version}
Provides:       tex(DANTE-Bold-Italic--texnansx.vf) = %{tl_version}
Provides:       tex(DANTE-Italic--texnansx.vf) = %{tl_version}
Provides:       tex(dantelogo.sty) = %{tl_version}, tex(OT1DANTE.fd) = %{tl_version}
Provides:       tex(T1DANTE.fd) = %{tl_version}

%description -n texlive-dantelogo
The DANTE font for the logo of DANTE (http://www.dante.de), the
German speaking TeX users group. The font includes only the
five characters d, a, n, t, and e. dantelogo.sty provides an
interface for LuaLaTeX/XeLaTeX/pdfLaTeX.

%package -n texlive-dantelogo-doc
Summary:        Documentation for dantelogo
Version:        svn38599

Provides:       tex-dantelogo-doc
AutoReqProv:    No

%description -n texlive-dantelogo-doc
Documentation for dantelogo

%package -n texlive-dejavu
Provides:       tex-dejavu = %{tl_version}
License:        LPPL
Summary:        LaTeX support for the DejaVu fonts
Version:        svn31771.2.34

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(keyval.sty)
Provides:       tex(dejavumono_il2.enc) = %{tl_version}, tex(dejavumono_lgr.enc) = %{tl_version}
Provides:       tex(dejavumono_ot1.enc) = %{tl_version}, tex(dejavumono_qx.enc) = %{tl_version}
Provides:       tex(dejavumono_t1-truetype.enc) = %{tl_version}
Provides:       tex(dejavumono_t1-type1.enc) = %{tl_version}
Provides:       tex(dejavumono_t2a.enc) = %{tl_version}, tex(dejavumono_t2b.enc) = %{tl_version}
Provides:       tex(dejavumono_t2c.enc) = %{tl_version}, tex(dejavumono_ts1.enc) = %{tl_version}
Provides:       tex(dejavumono_x2.enc) = %{tl_version}, tex(dejavusans_il2.enc) = %{tl_version}
Provides:       tex(dejavusans_lgr.enc) = %{tl_version}, tex(dejavusans_ot1.enc) = %{tl_version}
Provides:       tex(dejavusans_qx.enc) = %{tl_version}, tex(dejavusans_t1-truetype.enc) = %{tl_version}
Provides:       tex(dejavusans_t1-type1.enc) = %{tl_version}
Provides:       tex(dejavusans_t2a.enc) = %{tl_version}, tex(dejavusans_t2b.enc) = %{tl_version}
Provides:       tex(dejavusans_t2c.enc) = %{tl_version}, tex(dejavusans_ts1.enc) = %{tl_version}
Provides:       tex(dejavusans_x2.enc) = %{tl_version}, tex(dejavusanslight_il2.enc) = %{tl_version}
Provides:       tex(dejavusanslight_lgr.enc) = %{tl_version}
Provides:       tex(dejavusanslight_ot1.enc) = %{tl_version}
Provides:       tex(dejavusanslight_qx.enc) = %{tl_version}
Provides:       tex(dejavusanslight_t1-truetype.enc) = %{tl_version}
Provides:       tex(dejavusanslight_t1-type1.enc) = %{tl_version}
Provides:       tex(dejavusanslight_t2a.enc) = %{tl_version}
Provides:       tex(dejavusanslight_t2b.enc) = %{tl_version}
Provides:       tex(dejavusanslight_t2c.enc) = %{tl_version}
Provides:       tex(dejavusanslight_ts1.enc) = %{tl_version}
Provides:       tex(dejavusanslight_x2.enc) = %{tl_version}
Provides:       tex(dejavuserif_il2.enc) = %{tl_version}
Provides:       tex(dejavuserif_lgr.enc) = %{tl_version}
Provides:       tex(dejavuserif_ot1.enc) = %{tl_version}
Provides:       tex(dejavuserif_qx.enc) = %{tl_version}, tex(dejavuserif_t1-truetype.enc) = %{tl_version}
Provides:       tex(dejavuserif_t1-type1.enc) = %{tl_version}
Provides:       tex(dejavuserif_t2a.enc) = %{tl_version}
Provides:       tex(dejavuserif_t2b.enc) = %{tl_version}
Provides:       tex(dejavuserif_t2c.enc) = %{tl_version}
Provides:       tex(dejavuserif_ts1.enc) = %{tl_version}
Provides:       tex(dejavuserif_x2.enc) = %{tl_version}, tex(dejavu-truetype.map) = %{tl_version}
Provides:       tex(dejavu-type1.map) = %{tl_version}, tex(DejaVuSans-Bold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-lgr--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-lgr--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-lgr--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-lgr--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2b--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2c--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-x2--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-il2.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-qx--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-qx.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-t1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-x2.tfm) = %{tl_version}
Provides:       tex(DejaVuSans-Bold.ttf) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique.ttf) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight.ttf) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique.ttf) = %{tl_version}
Provides:       tex(DejaVuSans.ttf) = %{tl_version}, tex(DejaVuSansCondensed-Bold.ttf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique.ttf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique.ttf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed.ttf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold.ttf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique.ttf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique.ttf) = %{tl_version}
Provides:       tex(DejaVuSansMono.ttf) = %{tl_version}, tex(DejaVuSerif-Bold.ttf) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic.ttf) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic.ttf) = %{tl_version}
Provides:       tex(DejaVuSerif.ttf) = %{tl_version}, tex(DejaVuSerifCondensed-Bold.ttf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic.ttf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic.ttf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed.ttf) = %{tl_version}
Provides:       tex(DejaVuSans-Bold.pfb) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique.pfb) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight.pfb) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique.pfb) = %{tl_version}
Provides:       tex(DejaVuSans.pfb) = %{tl_version}, tex(DejaVuSansCondensed-Bold.pfb) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique.pfb) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique.pfb) = %{tl_version}
Provides:       tex(DejaVuSansCondensed.pfb) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold.pfb) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique.pfb) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique.pfb) = %{tl_version}
Provides:       tex(DejaVuSansMono.pfb) = %{tl_version}, tex(DejaVuSerif-Bold.pfb) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic.pfb) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic.pfb) = %{tl_version}
Provides:       tex(DejaVuSerif.pfb) = %{tl_version}, tex(DejaVuSerifCondensed-Bold.pfb) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic.pfb) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic.pfb) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed.pfb) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-BoldOblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2a.vf) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2b.vf) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2c.vf) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-ExtraLight-tlf-x2.vf) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-Oblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSans-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSansCondensed-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-lgr.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2a.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2b.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-t2c.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Bold-tlf-x2.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-lgr.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2a.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2b.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2c.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-x2.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-lgr.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2a.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2b.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2c.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-Oblique-tlf-x2.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-lgr.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2a.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2b.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-t2c.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSansMono-tlf-x2.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSerif-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-qx.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-t1.vf) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed-tlf-ts1.vf) = %{tl_version}
Provides:       tex(DejaVuSans.sty) = %{tl_version}, tex(DejaVuSansCondensed.sty) = %{tl_version}
Provides:       tex(DejaVuSansMono.sty) = %{tl_version}, tex(DejaVuSerif.sty) = %{tl_version}
Provides:       tex(DejaVuSerifCondensed.sty) = %{tl_version}
Provides:       tex(IL2DejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(IL2DejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(IL2DejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(IL2DejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(IL2DejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(LGRDejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(LGRDejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(LGRDejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(LGRDejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(LGRDejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(OT1DejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(OT1DejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(OT1DejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(OT1DejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(OT1DejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(QXDejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(QXDejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(QXDejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(QXDejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(QXDejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T1DejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(T1DejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T1DejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(T1DejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(T1DejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T2ADejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(T2ADejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T2ADejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(T2ADejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(T2ADejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T2BDejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(T2BDejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T2BDejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(T2BDejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(T2BDejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T2CDejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(T2CDejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T2CDejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(T2CDejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(T2CDejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(TS1DejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(TS1DejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(TS1DejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(TS1DejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(TS1DejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(X2DejaVuSans-TLF.fd) = %{tl_version}
Provides:       tex(X2DejaVuSansCondensed-TLF.fd) = %{tl_version}
Provides:       tex(X2DejaVuSansMono-TLF.fd) = %{tl_version}
Provides:       tex(X2DejaVuSerif-TLF.fd) = %{tl_version}
Provides:       tex(X2DejaVuSerifCondensed-TLF.fd) = %{tl_version}
Provides:       tex(dejavu.sty) = %{tl_version}

%description -n texlive-dejavu
The package contains LaTeX support for the DejaVu fonts, which
are derived from the Vera fonts but contain more characters and
styles. The fonts are included in the original TrueType format,
and in converted Type 1 format. The (currently) supported
encodings are: OT1, T1, IL2, TS1, T2*, X2, QX, and LGR. The
package doesn't (currently) support mathematics. More encodings
and/or features are expected.

%package -n texlive-dejavu-doc
Summary:        Documentation for dejavu
Version:        svn31771.2.34

Provides:       tex-dejavu-doc
AutoReqProv:    No

%description -n texlive-dejavu-doc
Documentation for dejavu

%package -n texlive-crossword
Provides:       tex-crossword = %{tl_version}
License:        Crossword
Summary:        Typeset crossword puzzles
Version:        svn32657.1.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amssymb.sty)
Provides:       tex(cwpuzzle.sty) = %{tl_version}

%description -n texlive-crossword
An extended grid-based puzzle package, designed to take all
input (both grid and clues) from the same file. The package can
typeset grids with holes in them (for advertisements, or other
sorts of stuff), and can deal with several sorts of puzzle: The
classical puzzle contains numbers for the words and clues for
the words to be filled in. The numbered puzzle contains numbers
in each cell where identical numbers represent identical
letters. The goal is to find out which number corresponds to
which letter. The fill-in type of puzzle consists of a grid and
a list of words. The goal is to place all words in the grid.
Sudoku and Kakuro puzzles involve filling in grids of numbers
according to their own rules. Format may be block-separated, or
separated by thick lines. Input to the package is somewhat
redundant: specification of the grid is separate from
specification of the clues (if they're necessary). The author
considers this style both 'natural' and robust.

%package -n texlive-crossword-doc
Summary:        Documentation for crossword
Version:        svn32657.1.9

Provides:       tex-crossword-doc
AutoReqProv:    No

%description -n texlive-crossword-doc
Documentation for crossword

%package -n texlive-crosswrd
Provides:       tex-crosswrd = %{tl_version}
License:        LPPL
Summary:        Macros for typesetting crossword puzzles
Version:        svn16896.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(crosswrd.sty) = %{tl_version}

%description -n texlive-crosswrd
The package provides a LaTeX method of typesetting crosswords,
and assists the composer ensure that the grid all goes together
properly. Brian Hamilton Kelly's original was written for LaTeX
2.09, and needed to be updated to run with current LaTeX.

%package -n texlive-crosswrd-doc
Summary:        Documentation for crosswrd
Version:        svn16896.3.0

Provides:       tex-crosswrd-doc
AutoReqProv:    No

%description -n texlive-crosswrd-doc
Documentation for crosswrd

%package -n texlive-c-pascal
Provides:       tex-c-pascal = %{tl_version}
License:        Public Domain
Summary:        Typeset Python, C and Pascal programs
Version:        svn18337.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cap.tex) = %{tl_version}, tex(cap_c.tex) = %{tl_version}
Provides:       tex(cap_comm.tex) = %{tl_version}, tex(cap_pas.tex) = %{tl_version}
Provides:       tex(cap_pyt.tex) = %{tl_version}

%description -n texlive-c-pascal
A TeX macro package for easy typesetting programs in Python, C
and Pascal. Program source files may also be input.

%package -n texlive-c-pascal-doc
Summary:        Documentation for c-pascal
Version:        svn18337.1.2

Provides:       tex-c-pascal-doc
AutoReqProv:    No

%description -n texlive-c-pascal-doc
Documentation for c-pascal

%package -n texlive-dad
Provides:       tex-dad = %{tl_version}
License:        LPPL
Summary:        Simple typesetting system for mixed Arabic/Latin documents
Version:        svn47027
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(dad.map) = %{tl_version}, tex(dadreal.tfm) = %{tl_version}
Provides:       tex(dadrealbold.tfm) = %{tl_version}, tex(dadrealmono.tfm) = %{tl_version}
Provides:       tex(Dad-bold.pfb) = %{tl_version}, tex(Dad-mono.pfb) = %{tl_version}
Provides:       tex(Dad.pfb) = %{tl_version}, tex(OT1dad.fd) = %{tl_version}
Provides:       tex(T1dad.fd) = %{tl_version}, tex(dad.sty) = %{tl_version}

%description -n texlive-dad
This package allows simple typesetting in Arabic script,
intended for mixed Arabic/Latin script usage in situations
where heavy-duty solutions are discouraged. The  system
operates with both Unicode and transliterated input, allowing
the user to choose the most appropriate approach for every
situation.

%package -n texlive-dad-doc
Summary:        Documentation for dad
Version:        svn47027
Provides:       tex-dad-doc
AutoReqProv:    No

%description -n texlive-dad-doc
Documentation for dad


%package -n texlive-ctex
Provides:       tex-ctex = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX classes and packages for Chinese typesetting
Version:        svn47595
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-ttfutils, tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty)
Requires:       tex(ctexpatch.sty), tex(fix-cm.sty), tex(everysel.sty), tex(fancyhdr.sty)
Requires:       tex(hyperref.sty), tex(zhnumber.sty)
Provides:       tex(ctexmakespa.tex) = %{tl_version}, tex(ctexspamacro.tex) = %{tl_version}
Provides:       tex(zhadobefonts.tex) = %{tl_version}, tex(zhfandolfonts.tex) = %{tl_version}
Provides:       tex(zhfounderfonts.tex) = %{tl_version}, tex(zhubuntufonts.tex) = %{tl_version}
Provides:       tex(zhwindowsfonts.tex) = %{tl_version}, tex(ctex-name-gbk.cfg) = %{tl_version}
Provides:       tex(ctex-name-utf8.cfg) = %{tl_version}, tex(ctex.cfg) = %{tl_version}
Provides:       tex(ctexopts.cfg) = %{tl_version}, tex(ctex-article.def) = %{tl_version}
Provides:       tex(ctex-book.def) = %{tl_version}, tex(ctex-c5size.clo) = %{tl_version}
Provides:       tex(ctex-cs4size.clo) = %{tl_version}, tex(ctex-report.def) = %{tl_version}
Provides:       tex(ctex.sty) = %{tl_version}, tex(ctexart.cls) = %{tl_version}
Provides:       tex(ctexbook.cls) = %{tl_version}, tex(ctexcap.sty) = %{tl_version}
Provides:       tex(ctexheading.sty) = %{tl_version}, tex(ctexhook.sty) = %{tl_version}
Provides:       tex(ctexpatch.sty) = %{tl_version}, tex(ctexrep.cls) = %{tl_version}
Provides:       tex(ctexsize.sty) = %{tl_version}, tex(ctexspa.def) = %{tl_version}
Provides:       tex(ctex-engine-luatex.def) = %{tl_version}
Provides:       tex(ctex-engine-pdftex.def) = %{tl_version}
Provides:       tex(ctex-engine-xetex.def) = %{tl_version}
Provides:       tex(c19rm.fd) = %{tl_version}, tex(c19sf.fd) = %{tl_version}
Provides:       tex(c19tt.fd) = %{tl_version}, tex(c70rm.fd) = %{tl_version}
Provides:       tex(c70sf.fd) = %{tl_version}, tex(c70tt.fd) = %{tl_version}
Provides:       tex(ctex-fontset-adobe.def) = %{tl_version}
Provides:       tex(ctex-fontset-fandol.def) = %{tl_version}
Provides:       tex(ctex-fontset-founder.def) = %{tl_version}
Provides:       tex(ctex-fontset-mac.def) = %{tl_version}
Provides:       tex(ctex-fontset-ubuntu.def) = %{tl_version}
Provides:       tex(ctex-fontset-windows.def) = %{tl_version}
Provides:       tex(ctex-fontset-windowsnew.def) = %{tl_version}
Provides:       tex(ctex-fontset-windowsold.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-article.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-book.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese-report.def) = %{tl_version}
Provides:       tex(ctex-scheme-chinese.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-article.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-book.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain-report.def) = %{tl_version}
Provides:       tex(ctex-scheme-plain.def) = %{tl_version}

%description -n texlive-ctex
ctex package

%package -n texlive-ctex-doc
Summary:        Documentation for ctex
Version:        svn47595
Provides:       tex-ctex-doc
AutoReqProv:    No
Requires:       tex-ttfutils-doc

%description -n texlive-ctex-doc
Documentation for ctex

%package -n texlive-ctex-faq-doc
Summary:        Documentation for ctex-faq
Version:        svn15878.0

Provides:       tex-ctex-faq-doc
AutoReqProv:    No

%description -n texlive-ctex-faq-doc
Documentation for ctex-faq

%package -n texlive-cyrplain
Provides:       tex-cyrplain = %{tl_version}
License:        LPPL
Summary:        cyrplain package
Version:        svn45692
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(cyrcmfnt.tex) = %{tl_version}, tex(cyrecfnt.tex) = %{tl_version}
Provides:       tex(cyrtex.cfg) = %{tl_version}, tex(cyrtex.tex) = %{tl_version}
Provides:       tex(plainenc.tex) = %{tl_version}, tex(txxdefs.tex) = %{tl_version}
Provides:       tex(txxextra.tex) = %{tl_version}

%description -n texlive-cyrplain
cyrplain package

%package -n texlive-cs
Provides:       tex-cs = %{tl_version}
License:        GPL+
Summary:        Czech/Slovak-tuned Computer Modern fonts
Version:        svn40785

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(xl2.enc) = %{tl_version}, tex(xl2f.enc) = %{tl_version}
Provides:       tex(xt2.enc) = %{tl_version}, tex(cs-a35-nodownload.map) = %{tl_version}
Provides:       tex(cs-a35-urwdownload.map) = %{tl_version}
Provides:       tex(cs-charter.map) = %{tl_version}, tex(csfonts.map) = %{tl_version}
Provides:       tex(pagd8z.tfm) = %{tl_version}, tex(pagdc8z.tfm) = %{tl_version}
Provides:       tex(pagdo8z.tfm) = %{tl_version}, tex(pagk8z.tfm) = %{tl_version}
Provides:       tex(pagkc8z.tfm) = %{tl_version}, tex(pagko8z.tfm) = %{tl_version}
Provides:       tex(pbkd8z.tfm) = %{tl_version}, tex(pbkdc8z.tfm) = %{tl_version}
Provides:       tex(pbkdi8z.tfm) = %{tl_version}, tex(pbkl8z.tfm) = %{tl_version}
Provides:       tex(pbklc8z.tfm) = %{tl_version}, tex(pbkli8z.tfm) = %{tl_version}
Provides:       tex(pcrb8u.tfm) = %{tl_version}, tex(pcrbc8u.tfm) = %{tl_version}
Provides:       tex(pcrbo8u.tfm) = %{tl_version}, tex(pcrr8u.tfm) = %{tl_version}
Provides:       tex(pcrrc8u.tfm) = %{tl_version}, tex(pcrro8u.tfm) = %{tl_version}
Provides:       tex(phvb8z.tfm) = %{tl_version}, tex(phvbc8z.tfm) = %{tl_version}
Provides:       tex(phvbn8z.tfm) = %{tl_version}, tex(phvbnc8z.tfm) = %{tl_version}
Provides:       tex(phvbo8z.tfm) = %{tl_version}, tex(phvbon8z.tfm) = %{tl_version}
Provides:       tex(phvr8z.tfm) = %{tl_version}, tex(phvrc8z.tfm) = %{tl_version}
Provides:       tex(phvrn8z.tfm) = %{tl_version}, tex(phvrnc8z.tfm) = %{tl_version}
Provides:       tex(phvro8z.tfm) = %{tl_version}, tex(phvron8z.tfm) = %{tl_version}
Provides:       tex(pncb8z.tfm) = %{tl_version}, tex(pncbc8z.tfm) = %{tl_version}
Provides:       tex(pncbi8z.tfm) = %{tl_version}, tex(pncr8z.tfm) = %{tl_version}
Provides:       tex(pncrc8z.tfm) = %{tl_version}, tex(pncri8z.tfm) = %{tl_version}
Provides:       tex(pplb8z.tfm) = %{tl_version}, tex(pplbc8z.tfm) = %{tl_version}
Provides:       tex(pplbi8z.tfm) = %{tl_version}, tex(pplr8z.tfm) = %{tl_version}
Provides:       tex(pplrc8z.tfm) = %{tl_version}, tex(pplri8z.tfm) = %{tl_version}
Provides:       tex(ptmb8z.tfm) = %{tl_version}, tex(ptmbc8z.tfm) = %{tl_version}
Provides:       tex(ptmbi8z.tfm) = %{tl_version}, tex(ptmr8z.tfm) = %{tl_version}
Provides:       tex(ptmrc8z.tfm) = %{tl_version}, tex(ptmri8z.tfm) = %{tl_version}
Provides:       tex(pzcmi8z.tfm) = %{tl_version}, tex(bchb8z.tfm) = %{tl_version}
Provides:       tex(bchbi8z.tfm) = %{tl_version}, tex(bchr8z.tfm) = %{tl_version}
Provides:       tex(bchri8z.tfm) = %{tl_version}, tex(rbchb.tfm) = %{tl_version}
Provides:       tex(rbchbi.tfm) = %{tl_version}, tex(rbchr.tfm) = %{tl_version}
Provides:       tex(rbchri.tfm) = %{tl_version}, tex(csb10.tfm) = %{tl_version}
Provides:       tex(csb12.tfm) = %{tl_version}, tex(csb17.tfm) = %{tl_version}
Provides:       tex(csb5.tfm) = %{tl_version}, tex(csb6.tfm) = %{tl_version}
Provides:       tex(csb7.tfm) = %{tl_version}, tex(csb8.tfm) = %{tl_version}
Provides:       tex(csb9.tfm) = %{tl_version}, tex(csbx10.tfm) = %{tl_version}
Provides:       tex(csbx12.tfm) = %{tl_version}, tex(csbx5.tfm) = %{tl_version}
Provides:       tex(csbx6.tfm) = %{tl_version}, tex(csbx7.tfm) = %{tl_version}
Provides:       tex(csbx8.tfm) = %{tl_version}, tex(csbx9.tfm) = %{tl_version}
Provides:       tex(csbxsl10.tfm) = %{tl_version}, tex(csbxsl12.tfm) = %{tl_version}
Provides:       tex(csbxsl5.tfm) = %{tl_version}, tex(csbxsl6.tfm) = %{tl_version}
Provides:       tex(csbxsl7.tfm) = %{tl_version}, tex(csbxsl8.tfm) = %{tl_version}
Provides:       tex(csbxsl9.tfm) = %{tl_version}, tex(csbxti10.tfm) = %{tl_version}
Provides:       tex(csbxti12.tfm) = %{tl_version}, tex(csbxti17.tfm) = %{tl_version}
Provides:       tex(cscsc10.tfm) = %{tl_version}, tex(cscsc12.tfm) = %{tl_version}
Provides:       tex(cscsc17.tfm) = %{tl_version}, tex(cscsc8.tfm) = %{tl_version}
Provides:       tex(cscsc9.tfm) = %{tl_version}, tex(csdunh10.tfm) = %{tl_version}
Provides:       tex(csdunh12.tfm) = %{tl_version}, tex(csdunh17.tfm) = %{tl_version}
Provides:       tex(csdunh5.tfm) = %{tl_version}, tex(csdunh6.tfm) = %{tl_version}
Provides:       tex(csdunh7.tfm) = %{tl_version}, tex(csdunh8.tfm) = %{tl_version}
Provides:       tex(csdunh9.tfm) = %{tl_version}, tex(csff10.tfm) = %{tl_version}
Provides:       tex(csfi10.tfm) = %{tl_version}, tex(csfib10.tfm) = %{tl_version}
Provides:       tex(csfib12.tfm) = %{tl_version}, tex(csfib8.tfm) = %{tl_version}
Provides:       tex(csfib9.tfm) = %{tl_version}, tex(csinch.tfm) = %{tl_version}
Provides:       tex(csitt10.tfm) = %{tl_version}, tex(csitt12.tfm) = %{tl_version}
Provides:       tex(csitt17.tfm) = %{tl_version}, tex(csitt8.tfm) = %{tl_version}
Provides:       tex(csitt9.tfm) = %{tl_version}, tex(csr10.tfm) = %{tl_version}
Provides:       tex(csr12.tfm) = %{tl_version}, tex(csr17.tfm) = %{tl_version}
Provides:       tex(csr5.tfm) = %{tl_version}, tex(csr6.tfm) = %{tl_version}
Provides:       tex(csr7.tfm) = %{tl_version}, tex(csr8.tfm) = %{tl_version}
Provides:       tex(csr9.tfm) = %{tl_version}, tex(cssl10.tfm) = %{tl_version}
Provides:       tex(cssl12.tfm) = %{tl_version}, tex(cssl17.tfm) = %{tl_version}
Provides:       tex(cssl5.tfm) = %{tl_version}, tex(cssl6.tfm) = %{tl_version}
Provides:       tex(cssl7.tfm) = %{tl_version}, tex(cssl8.tfm) = %{tl_version}
Provides:       tex(cssl9.tfm) = %{tl_version}, tex(cssltt10.tfm) = %{tl_version}
Provides:       tex(cssltt12.tfm) = %{tl_version}, tex(cssltt8.tfm) = %{tl_version}
Provides:       tex(cssltt9.tfm) = %{tl_version}, tex(csss10.tfm) = %{tl_version}
Provides:       tex(csss12.tfm) = %{tl_version}, tex(csss17.tfm) = %{tl_version}
Provides:       tex(csss8.tfm) = %{tl_version}, tex(csss9.tfm) = %{tl_version}
Provides:       tex(csssbx10.tfm) = %{tl_version}, tex(csssbx12.tfm) = %{tl_version}
Provides:       tex(csssbx17.tfm) = %{tl_version}, tex(csssbx9.tfm) = %{tl_version}
Provides:       tex(csssdc10.tfm) = %{tl_version}, tex(csssi10.tfm) = %{tl_version}
Provides:       tex(csssi12.tfm) = %{tl_version}, tex(csssi17.tfm) = %{tl_version}
Provides:       tex(csssi8.tfm) = %{tl_version}, tex(csssi9.tfm) = %{tl_version}
Provides:       tex(csssq8.tfm) = %{tl_version}, tex(csssqi8.tfm) = %{tl_version}
Provides:       tex(cstcsc10.tfm) = %{tl_version}, tex(cstcsc12.tfm) = %{tl_version}
Provides:       tex(cstcsc17.tfm) = %{tl_version}, tex(csti10.tfm) = %{tl_version}
Provides:       tex(csti12.tfm) = %{tl_version}, tex(csti17.tfm) = %{tl_version}
Provides:       tex(csti7.tfm) = %{tl_version}, tex(csti8.tfm) = %{tl_version}
Provides:       tex(csti9.tfm) = %{tl_version}, tex(cstt10.tfm) = %{tl_version}
Provides:       tex(cstt12.tfm) = %{tl_version}, tex(cstt8.tfm) = %{tl_version}
Provides:       tex(cstt9.tfm) = %{tl_version}, tex(csu10.tfm) = %{tl_version}
Provides:       tex(csu12.tfm) = %{tl_version}, tex(csu17.tfm) = %{tl_version}
Provides:       tex(csu7.tfm) = %{tl_version}, tex(csu8.tfm) = %{tl_version}
Provides:       tex(csu9.tfm) = %{tl_version}, tex(csvtt10.tfm) = %{tl_version}
Provides:       tex(csvtt12.tfm) = %{tl_version}, tex(csvtt8.tfm) = %{tl_version}
Provides:       tex(csvtt9.tfm) = %{tl_version}, tex(icscsc10.tfm) = %{tl_version}
Provides:       tex(icstt8.tfm) = %{tl_version}, tex(ilcsss8.tfm) = %{tl_version}
Provides:       tex(ilcsssb8.tfm) = %{tl_version}, tex(ilcsssi8.tfm) = %{tl_version}
Provides:       tex(lcsss8.tfm) = %{tl_version}, tex(lcsssb8.tfm) = %{tl_version}
Provides:       tex(lcsssi8.tfm) = %{tl_version}, tex(csb10.pfb) = %{tl_version}
Provides:       tex(csbx10.pfb) = %{tl_version}, tex(csbx12.pfb) = %{tl_version}
Provides:       tex(csbx5.pfb) = %{tl_version}, tex(csbx6.pfb) = %{tl_version}
Provides:       tex(csbx7.pfb) = %{tl_version}, tex(csbx8.pfb) = %{tl_version}
Provides:       tex(csbx9.pfb) = %{tl_version}, tex(csbxsl10.pfb) = %{tl_version}
Provides:       tex(csbxti10.pfb) = %{tl_version}, tex(cscsc10.pfb) = %{tl_version}
Provides:       tex(csdunh10.pfb) = %{tl_version}, tex(csff10.pfb) = %{tl_version}
Provides:       tex(csfi10.pfb) = %{tl_version}, tex(csfib8.pfb) = %{tl_version}
Provides:       tex(csinch.pfb) = %{tl_version}, tex(csitt10.pfb) = %{tl_version}
Provides:       tex(csr10.pfb) = %{tl_version}, tex(csr12.pfb) = %{tl_version}
Provides:       tex(csr17.pfb) = %{tl_version}, tex(csr5.pfb) = %{tl_version}
Provides:       tex(csr6.pfb) = %{tl_version}, tex(csr7.pfb) = %{tl_version}
Provides:       tex(csr8.pfb) = %{tl_version}, tex(csr9.pfb) = %{tl_version}
Provides:       tex(cssl10.pfb) = %{tl_version}, tex(cssl12.pfb) = %{tl_version}
Provides:       tex(cssl8.pfb) = %{tl_version}, tex(cssl9.pfb) = %{tl_version}
Provides:       tex(cssltt10.pfb) = %{tl_version}, tex(csss10.pfb) = %{tl_version}
Provides:       tex(csss12.pfb) = %{tl_version}, tex(csss17.pfb) = %{tl_version}
Provides:       tex(csss8.pfb) = %{tl_version}, tex(csss9.pfb) = %{tl_version}
Provides:       tex(csssbx10.pfb) = %{tl_version}, tex(csssdc10.pfb) = %{tl_version}
Provides:       tex(csssi10.pfb) = %{tl_version}, tex(csssi12.pfb) = %{tl_version}
Provides:       tex(csssi17.pfb) = %{tl_version}, tex(csssi8.pfb) = %{tl_version}
Provides:       tex(csssi9.pfb) = %{tl_version}, tex(csssq8.pfb) = %{tl_version}
Provides:       tex(csssqi8.pfb) = %{tl_version}, tex(cstcsc10.pfb) = %{tl_version}
Provides:       tex(csti10.pfb) = %{tl_version}, tex(csti12.pfb) = %{tl_version}
Provides:       tex(csti7.pfb) = %{tl_version}, tex(csti8.pfb) = %{tl_version}
Provides:       tex(csti9.pfb) = %{tl_version}, tex(cstt10.pfb) = %{tl_version}
Provides:       tex(cstt12.pfb) = %{tl_version}, tex(cstt8.pfb) = %{tl_version}
Provides:       tex(cstt9.pfb) = %{tl_version}, tex(csu10.pfb) = %{tl_version}
Provides:       tex(csvtt10.pfb) = %{tl_version}, tex(pagdc8z.vf) = %{tl_version}
Provides:       tex(pagkc8z.vf) = %{tl_version}, tex(pbkdc8z.vf) = %{tl_version}
Provides:       tex(pbklc8z.vf) = %{tl_version}, tex(pcrbc8u.vf) = %{tl_version}
Provides:       tex(pcrrc8u.vf) = %{tl_version}, tex(phvbc8z.vf) = %{tl_version}
Provides:       tex(phvbnc8z.vf) = %{tl_version}, tex(phvrc8z.vf) = %{tl_version}
Provides:       tex(phvrnc8z.vf) = %{tl_version}, tex(pncbc8z.vf) = %{tl_version}
Provides:       tex(pncrc8z.vf) = %{tl_version}, tex(pplbc8z.vf) = %{tl_version}
Provides:       tex(pplrc8z.vf) = %{tl_version}, tex(ptmbc8z.vf) = %{tl_version}
Provides:       tex(ptmrc8z.vf) = %{tl_version}, tex(bchb8z.vf) = %{tl_version}
Provides:       tex(bchbi8z.vf) = %{tl_version}, tex(bchr8z.vf) = %{tl_version}
Provides:       tex(bchri8z.vf) = %{tl_version}

%description -n texlive-cs
The fonts are provided as Metafont source; Type 1 format
versions (csfonts-t1) are also available.

%package -n texlive-csbulletin
Provides:       tex-csbulletin = %{tl_version}
License:        LPPL
Summary:        LaTeX class for articles submitted to the CSTUG Bulletin (Zpravodaj)
Version:        svn43277
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(babel.sty), tex(fontenc.sty), tex(lmodern.sty), tex(mflogo.sty)
Requires:       tex(ifpdf.sty), tex(microtype.sty), tex(array.sty), tex(fancyvrb.sty)
Requires:       tex(verbatim.sty), tex(encxvlna.sty)
Provides:       tex(csbulacronym.sty) = %{tl_version}, tex(csbulletin.cls) = %{tl_version}

%description -n texlive-csbulletin
The package provides the class for articles for the CSTUG
Bulletin (Zpravodaj Ceskoslovenskeho sdruzeni uzivatelu TeXu).
You can see the structure of a document by looking to the
source file of the manual.

%package -n texlive-csbulletin-doc
Summary:        Documentation for csbulletin
Version:        svn43277
Provides:       tex-csbulletin-doc
AutoReqProv:    No

%description -n texlive-csbulletin-doc
Documentation for csbulletin

%package -n texlive-cstex-doc
Summary:        Documentation for cstex
Version:        svn41301

Provides:       tex-cstex-doc
AutoReqProv:    No

%description -n texlive-cstex-doc
Documentation for cstex

%package -n texlive-csquotes-de-doc
Summary:        Documentation for csquotes-de
Version:        svn23371.1.01

Provides:       tex-csquotes-de-doc
AutoReqProv:    No

%description -n texlive-csquotes-de-doc
Documentation for csquotes-de

%package -n texlive-dehyph-exptl
Provides:       tex-dehyph-exptl = %{tl_version}
License:        LPPL
Summary:        Experimental hyphenation patterns for the German language
Version:        svn47240
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8
Provides:       tex(dehyphn-x-2014-05-21.tex) = %{tl_version}
Provides:       tex(dehypht-x-2014-05-21.tex) = %{tl_version}
Provides:       tex(dehyphts-x-2014-05-21.tex) = %{tl_version}

%description -n texlive-dehyph-exptl
The package provides experimental hyphenation patterns for the
German language, covering both traditional and reformed
orthography. The patterns can be used with packages Babel and
hyphsubst from the Oberdiek bundle. Dieses Paket enthalt
experimentelle Trennmuster fur die deutsche Sprache. Die
Trennmuster decken das in Deutschland, Osterreich und der
Schweiz gebrauchliche Standarddeutsch in der traditionellen und
reformierten Rechtschreibung ab und konnen mit den Paketen
Babel und hyphsubst aus dem Oberdiek-Bundel verwendet werden.

%post -n texlive-dehyph-exptl
if [ $1 -gt 0 ] ; then
sed -i '/german-x-2014-05-21.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "german-x-2014-05-21 dehypht-x-2014-05-21.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=german-x-latest/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=german-x-latest" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{german-x-2014-05-21}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{german-x-2014-05-21}{dehypht-x-2014-05-21.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{german-x-latest}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{german-x-latest}{dehypht-x-2014-05-21.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/ngerman-x-2014-05-21.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "ngerman-x-2014-05-21 dehyphn-x-2014-05-21.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=ngerman-x-latest/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=ngerman-x-latest" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{ngerman-x-2014-05-21}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{ngerman-x-2014-05-21}{dehyphn-x-2014-05-21.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{ngerman-x-latest}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{ngerman-x-latest}{dehyphn-x-2014-05-21.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-dehyph-exptl
if [ $1 == 0 ] ; then
sed -i '/german-x-2014-05-21.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=german-x-latest/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{german-x-2014-05-21}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{german-x-latest}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/ngerman-x-2014-05-21.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=ngerman-x-latest/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{ngerman-x-2014-05-21}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{ngerman-x-latest}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-dehyph-exptl-doc
Summary:        Documentation for dehyph-exptl
Version:        svn47240
Provides:       tex-dehyph-exptl-doc
AutoReqProv:    No
Requires:       tex-hyph-utf8-doc

%description -n texlive-dehyph-exptl-doc
Documentation for dehyph-exptl

%package -n texlive-ctib
Provides:       tex-ctib = %{tl_version}
License:        GPL+
Summary:        Tibetan for TeX and LATeX2e
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty)
Provides:       tex(ctib.tfm) = %{tl_version}, tex(ctib.sty) = %{tl_version}
Provides:       tex(ctib.tex) = %{tl_version}, tex(lctctib.fd) = %{tl_version}
Provides:       tex(lctenc.def) = %{tl_version}

%description -n texlive-ctib
A package using a modified version of Sirlin's Tibetan font. An
advantage of this Tibetan implementation is that all consonant
clusters are formed by TeX and Metafont. No external
preprocessor is needed.

%package -n texlive-ctib-doc
Summary:        Documentation for ctib
Version:        svn15878.0

Provides:       tex-ctib-doc
AutoReqProv:    No

%description -n texlive-ctib-doc
Documentation for ctib

%package -n texlive-cursolatex-doc
Summary:        Documentation for cursolatex
Version:        svn24139.0

Provides:       tex-cursolatex-doc
AutoReqProv:    No

%description -n texlive-cursolatex-doc
Documentation for cursolatex

%package -n texlive-crop
Provides:       tex-crop = %{tl_version}
License:        LPPL
Summary:        Support for cropmarks
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(graphics.sty)
Provides:       tex(crop.sty) = %{tl_version}

%description -n texlive-crop
A package providing corner marks for camera alignment as well
as for trimming paper stacks, and additional page information
on every page if required. Most macros are easily adaptable to
personal preferences. An option is provided for selectively
suppressing graphics or text, which may be useful for printing
just colour graphics on a colour laser printer and the rest on
a cheap mono laser printer. A page info line contains the time
and a new cropmarks index and is printed at the top of the
page. A configuration command is provided for the info line
font. Options for better collaboration with dvips, pdftex and
vtex are provided.

%package -n texlive-crop-doc
Summary:        Documentation for crop
Version:        svn15878.1.5

Provides:       tex-crop-doc
AutoReqProv:    No

%description -n texlive-crop-doc
Documentation for crop

%package -n texlive-ctable
Provides:       tex-ctable = %{tl_version}
License:        LPPL
Summary:        Flexible typesetting of table and figure floats using key/value directives
Version:        svn38672

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(etoolbox.sty), tex(xcolor.sty), tex(xkeyval.sty)
Requires:       tex(array.sty), tex(tabularx.sty), tex(booktabs.sty), tex(rotating.sty)
Requires:       tex(transparent.sty)
Provides:       tex(ctable.sty) = %{tl_version}

%description -n texlive-ctable
Provides commands to typeset centered, left- or right-aligned
table and (multiple-)figure floats, with footnotes. Instead of
an environment, a command with 4 arguments is used; the first
is optional and is used for key,value pairs generating
variations on the defaults and offering a route for future
extensions.

%package -n texlive-ctable-doc
Summary:        Documentation for ctable
Version:        svn38672

Provides:       tex-ctable-doc
AutoReqProv:    No

%description -n texlive-ctable-doc
Documentation for ctable

%package -n texlive-curve
Provides:       tex-curve = %{tl_version}
License:        LPPL
Summary:        A class for making curriculum vitae
Version:        svn20745.1.16

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ltxtable.sty), tex(ifthen.sty), tex(calc.sty), tex(filehook.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(curve.cls) = %{tl_version}

%description -n texlive-curve
CurVe is a class for writing a CV, with configuration for the
language in which you write. The class provides a set of
commands to create rubrics, entries in these rubrics etc. CurVe
then format the CV (possibly splitting it onto multiple pages,
repeating the titles etc), which is usually the most painful
part of CV writing. Another nice feature of CurVe is its
ability to manage different CV 'flavours' simultaneously. It is
often the case that you want to maintain slightly divergent
versions of your CV at the same time, in order to emphasize on
different aspects of your background. CurVe also comes with
support for use with AUC-TeX.

%package -n texlive-curve-doc
Summary:        Documentation for curve
Version:        svn20745.1.16

Provides:       tex-curve-doc
AutoReqProv:    No

%description -n texlive-curve-doc
Documentation for curve

%package -n texlive-curve2e
Provides:       tex-curve2e = %{tl_version}
License:        LPPL 1.3
Summary:        Extensions for package pict2e
Version:        svn37839.1.60

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(pict2e.sty)
Provides:       tex(curve2e.sty) = %{tl_version}

%description -n texlive-curve2e
The package extends the drawing capacities of the pict2e that
serves as a LaTeX 2e replacement for picture mode. In
particular, curve2e introduces new macros for lines and
vectors, new specifications for line terminations and joins,
arcs with any angular aperture, arcs with arrows at one or both
ends, generic curves specified with their nodes and the tangent
direction at these nodes.

%package -n texlive-curve2e-doc
Summary:        Documentation for curve2e
Version:        svn37839.1.60

Provides:       tex-curve2e-doc
AutoReqProv:    No

%description -n texlive-curve2e-doc
Documentation for curve2e

%package -n texlive-curves
Provides:       tex-curves = %{tl_version}
License:        LPPL
Summary:        Curves for LaTeX picture environment
Version:        svn45255
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(curves.sty) = %{tl_version}, tex(curvesls.sty) = %{tl_version}

%description -n texlive-curves
The draws curves in the standard LaTeX picture environment
using parabolas between data points with continuous slope at
joins; for circles and arcs, it uses up to 16 parabolas. The
package also draws symbols or dash patterns along curves. The
package provides facilities equivalent to technical pens with
compasses and French curves. Curves consist of short secants
drawn by overlapping disks or line-drawing \special commands
selected by package options.

%package -n texlive-curves-doc
Summary:        Documentation for curves
Version:        svn45255
Provides:       tex-curves-doc
AutoReqProv:    No

%description -n texlive-curves-doc
Documentation for curves

%package -n texlive-dcpic
Provides:       tex-dcpic = %{tl_version}
License:        LPPL 1.3
Summary:        Commutative diagrams in a LaTeX and TeX documents
Version:        svn30206.5.0.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dcpic.sty) = %{tl_version}, tex(europroc.cls) = %{tl_version}

%description -n texlive-dcpic
DCpic is a package for typesetting Commutative Diagrams within
a LaTeX and TeX documents. Its distinguishing features are: a
powerful graphical engine, the PiCTeX package; an easy
specification syntax in which a commutative diagram is
described in terms of its objects and its arrows (morphism),
positioned in a Cartesian coordinate system.

%package -n texlive-dcpic-doc
Summary:        Documentation for dcpic
Version:        svn30206.5.0.0

Provides:       tex-dcpic-doc
AutoReqProv:    No

%description -n texlive-dcpic-doc
Documentation for dcpic


%package -n texlive-cprotect
Provides:       tex-cprotect = %{tl_version}
License:        LPPL 1.3
Summary:        Allow verbatim, etc., in macro arguments
Version:        svn21209.1.0e

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(suffix.sty)
Provides:       tex(cprotect.sty) = %{tl_version}

%description -n texlive-cprotect
The package defines the macro \cprotect that makes a following
macro proof against verbatim in its argument; as, for example,
\cprotect\section{\verb"foo"} A similar macro \cprotEnv
(applied to the \begin of an environment) sanitises the
behavior of fragile environments. Moving arguments, and
corresponding "tables of ..." work happily.

%package -n texlive-cprotect-doc
Summary:        Documentation for cprotect
Version:        svn21209.1.0e

Provides:       tex-cprotect-doc
AutoReqProv:    No

%description -n texlive-cprotect-doc
Documentation for cprotect

%package -n texlive-crbox
Provides:       tex-crbox = %{tl_version}
License:        LPPL
Summary:        Boxes with crossed corners
Version:        svn29803.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(biditools.sty)
Provides:       tex(crbox.sty) = %{tl_version}

%description -n texlive-crbox
The package implements a \crbox command which produces boxes
with crossing lines at the corners.

%package -n texlive-crbox-doc
Summary:        Documentation for crbox
Version:        svn29803.0.1

Provides:       tex-crbox-doc
AutoReqProv:    No

%description -n texlive-crbox-doc
Documentation for crbox

%package -n texlive-crossreference
Provides:       tex-crossreference = %{tl_version}
License:        LPPL
Summary:        Crossreferences within documents
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(crossreference.sty) = %{tl_version}

%description -n texlive-crossreference
The package defines cross-references (essentially 'grand' label
references), which may be listed in a table of cross-
references.

%package -n texlive-crossreference-doc
Summary:        Documentation for crossreference
Version:        svn15878.0

Provides:       tex-crossreference-doc
AutoReqProv:    No

%description -n texlive-crossreference-doc
Documentation for crossreference

%package -n texlive-csquotes
Provides:       tex-csquotes = %{tl_version}
License:        LPPL 1.3
Summary:        Context sensitive quotation facilities
Version:        svn47564
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty), tex(keyval.sty)
Provides:       tex(csq-compat.def) = %{tl_version}, tex(csquotes.cfg) = %{tl_version}
Provides:       tex(csquotes.def) = %{tl_version}, tex(csquotes.sty) = %{tl_version}

%description -n texlive-csquotes
This package provides advanced facilities for inline and
display quotations. It is designed for a wide range of tasks
ranging from the most simple applications to the more complex
demands of formal quotations. The facilities include commands,
environments, and user-definable 'smart quotes' which
dynamically adjust to their context. Quotation marks are
switched automatically if quotations are nested and they can be
adjusted to the current language if the babel package is
available. There are additional facilities designed to cope
with the more specific demands of academic writing, especially
in the humanities and the social sciences. All quote styles as
well as the optional active quotes are freely configurable. The
package is dependent on e-TeX, and requires the author's
etoolbox package.

%package -n texlive-csquotes-doc
Summary:        Documentation for csquotes
Version:        svn47564
Provides:       tex-csquotes-doc
AutoReqProv:    No

%description -n texlive-csquotes-doc
Documentation for csquotes

%package -n texlive-csvsimple
Provides:       tex-csvsimple = %{tl_version}
License:        LPPL 1.3
Summary:        Simple CSV file processing
Version:        svn41597
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pgfkeys.sty), tex(ifthen.sty)
Provides:       tex(csvsimple.sty) = %{tl_version}

%description -n texlive-csvsimple
The package provides a simple LaTeX interface for the
processing of files with comma separated values (CSV); it
relies on the key value syntax supported by pgfkeys to simplify
usage. Filtering and table generation is especially supported;
however, this lightweight tool offers no support for data
sorting or data base storage.

%package -n texlive-csvsimple-doc
Summary:        Documentation for csvsimple
Version:        svn41597
Provides:       tex-csvsimple-doc
AutoReqProv:    No

%description -n texlive-csvsimple-doc
Documentation for csvsimple

%package -n texlive-cuisine
Provides:       tex-cuisine = %{tl_version}
License:        LPPL
Summary:        Typeset recipes
Version:        svn34453.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(nicefrac.sty)
Provides:       tex(cuisine.sty) = %{tl_version}

%description -n texlive-cuisine
Typeset recipes with the ingredients lined up with their method
step (somewhat similarly to the layout used in cooking).

%package -n texlive-cuisine-doc
Summary:        Documentation for cuisine
Version:        svn34453.0.7

Provides:       tex-cuisine-doc
AutoReqProv:    No

%description -n texlive-cuisine-doc
Documentation for cuisine

%package -n texlive-currfile
Provides:       tex-currfile = %{tl_version}
License:        LPPL 1.3
Summary:        Provide file name and path of input files
Version:        svn40725

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(filehook.sty)
Provides:       tex(currfile-abspath.sty) = %{tl_version}
Provides:       tex(currfile.sty) = %{tl_version}

%description -n texlive-currfile
The package provides macros holding file name information
(directory, base name, extension, full name and full path) for
files read by LaTeX \input and \include macros; it uses the
file hooks provided by the author's filehook. In particular, it
restores the parent file name after the trailing \clearpage of
an \included file; as a result, the macros may be usefully
employed in the page header and footer of the last printed page
of such a file. The depth of inclusion is made available,
together with the "parent" (including file) and "parents" (all
including files to the root of the tree). The package
supersedes FiNK.

%package -n texlive-currfile-doc
Summary:        Documentation for currfile
Version:        svn40725

Provides:       tex-currfile-doc
AutoReqProv:    No

%description -n texlive-currfile-doc
Documentation for currfile

%package -n texlive-currvita
Provides:       tex-currvita = %{tl_version}
License:        GPL+
Summary:        Typeset a curriculum vitae
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(currvita.sty) = %{tl_version}

%description -n texlive-currvita
Currvita is a package rather than a class (like most other
curriculum vitae offerings). The author considers that a
curriculum vitae can quite reasonably form part of another
document (such as a letter, or a dissertation).

%package -n texlive-currvita-doc
Summary:        Documentation for currvita
Version:        svn15878.0

Provides:       tex-currvita-doc
AutoReqProv:    No

%description -n texlive-currvita-doc
Documentation for currvita

%package -n texlive-cutwin
Provides:       tex-cutwin = %{tl_version}
License:        LPPL 1.3
Summary:        Cut a window in a paragraph, typeset material in it
Version:        svn29803.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cutwin.sty) = %{tl_version}

%description -n texlive-cutwin
The package provides facilities to cut windows out of
paragraphs, and to typeset text or other material in the
window. The window may be rectangular, or may have other sorts
of shape.

%package -n texlive-cutwin-doc
Summary:        Documentation for cutwin
Version:        svn29803.0.1

Provides:       tex-cutwin-doc
AutoReqProv:    No

%description -n texlive-cutwin-doc
Documentation for cutwin

%package -n texlive-cv
Provides:       tex-cv = %{tl_version}
License:        GPL+
Summary:        A package for creating a curriculum vitae
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(CV.sty) = %{tl_version}

%description -n texlive-cv
The package is distributed with two example files; they (and
their formatted output) constitute the only real documentation.
Note that cv is just a package: you choose the overall
formatting by deciding which class to use, while the package
provides the detailed formatting.

%package -n texlive-cv-doc
Summary:        Documentation for cv
Version:        svn15878.0

Provides:       tex-cv-doc
AutoReqProv:    No

%description -n texlive-cv-doc
Documentation for cv

%package -n texlive-cv4tw
Provides:       tex-cv4tw = %{tl_version}
License:        MIT
Summary:        LaTeX CV class, with extended details
Version:        svn34577.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(boxedminipage.sty), tex(geometry.sty)
Requires:       tex(libertine.sty), tex(multicol.sty), tex(pifont.sty), tex(pbox.sty)
Requires:       tex(needspace.sty), tex(amssymb.sty), tex(fontspec.sty), tex(fontawesome.sty)
Requires:       tex(realboxes.sty), tex(array.sty), tex(forloop.sty), tex(newenviron.sty)
Requires:       tex(etoolbox.sty), tex(xcolor.sty), tex(graphicx.sty), tex(xstring.sty)
Requires:       tex(fancyhdr.sty), tex(lastpage.sty), tex(hyperref.sty)
Provides:       tex(cv4tw-scheme.sty) = %{tl_version}, tex(cv4tw-theme-compact.sty) = %{tl_version}
Provides:       tex(cv4tw-theme-core.sty) = %{tl_version}
Provides:       tex(cv4tw-theme-sharp.sty) = %{tl_version}
Provides:       tex(cv4tw-theme-simple.sty) = %{tl_version}
Provides:       tex(cv4tw.cls) = %{tl_version}

%description -n texlive-cv4tw
The class offers entries for assets and social networks;
customizable styles are provided. The class comes with no
documentation, but a worked example offers some guidance.

%package -n texlive-cv4tw-doc
Summary:        Documentation for cv4tw
Version:        svn34577.0.2

Provides:       tex-cv4tw-doc
AutoReqProv:    No

%description -n texlive-cv4tw-doc
Documentation for cv4tw

%package -n texlive-cweb-latex
Provides:       tex-cweb-latex = %{tl_version}
License:        GPL+
Summary:        A LaTeX version of CWEB
Version:        svn28878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty)
Provides:       tex(cwbl-german.sty) = %{tl_version}, tex(cweb.cls) = %{tl_version}
Provides:       tex(cwebarray.sty) = %{tl_version}, tex(cwebbase.tex) = %{tl_version}
Provides:       tex(keyvald.sty) = %{tl_version}

%description -n texlive-cweb-latex
This bundle allows marking-up of CWEB code in LaTeX. The
distribution includes the "Counting Words" program distributed
with CWEB, edited to run with LaTeX.

%package -n texlive-cweb-latex-doc
Summary:        Documentation for cweb-latex
Version:        svn28878.0

Provides:       tex-cweb-latex-doc
AutoReqProv:    No

%description -n texlive-cweb-latex-doc
Documentation for cweb-latex

%package -n texlive-cyber
Provides:       tex-cyber = %{tl_version}
License:        MIT
Summary:        Annotate compliance with cybersecurity requirements
Version:        svn46776
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(longtable.sty), tex(color.sty), tex(index.sty), tex(fancyhdr.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(cyber.sty) = %{tl_version}

%description -n texlive-cyber
This LaTeX package helps you write documents indicating your
compliance with cybersecurity requirements. It also helps you
format your document in a form suitable inside the U.S.
Department of Defense, by attaching distribution statements,
destruction notices, organization logos, and security labels to
it.

%package -n texlive-cyber-doc
Summary:        Documentation for cyber
Version:        svn46776
Provides:       tex-cyber-doc
AutoReqProv:    No

%description -n texlive-cyber-doc
Documentation for cyber

%package -n texlive-cybercic
Provides:       tex-cybercic = %{tl_version}
License:        MIT
Summary:        "Controls in Contents" for the cyber package
Version:        svn37659.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cybercic.sty) = %{tl_version}

%description -n texlive-cybercic
This package is used in concert with the cyber package to make
documents with annotations of compliance with cybersecurity
requirements. "cic" stands for "Controls in Contents", and when
you include this package, some notations of compliance are
added to section names as seen in the table of contents of the
final document. It also makes your document more brittle in
unexpected ways: for example, when you use cybercic in the same
document as hyperref, you cannot use any formatting in your
section titles. So don't use cybercic unless you need to.

%package -n texlive-cybercic-doc
Summary:        Documentation for cybercic
Version:        svn37659.2.1

Provides:       tex-cybercic-doc
AutoReqProv:    No

%description -n texlive-cybercic-doc
Documentation for cybercic

%package -n texlive-dashbox
Provides:       tex-dashbox = %{tl_version}
License:        LPPL
Summary:        Draw dashed boxes
Version:        svn23425.1.14

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(ifthen.sty)
Provides:       tex(dashbox.sty) = %{tl_version}

%description -n texlive-dashbox
The package can draw boxes that perform like \framebox or
\fbox, but use dashed lines. The package can also draw (an
illusion of) vertical stacks of boxes.

%package -n texlive-dashbox-doc
Summary:        Documentation for dashbox
Version:        svn23425.1.14

Provides:       tex-dashbox-doc
AutoReqProv:    No

%description -n texlive-dashbox-doc
Documentation for dashbox

%package -n texlive-dashrule
Provides:       tex-dashrule = %{tl_version}
License:        LPPL
Summary:        Draw dashed rules
Version:        svn29579.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifmtarg.sty)
Provides:       tex(dashrule.sty) = %{tl_version}

%description -n texlive-dashrule
The dashrule package makes it easy to draw a huge variety of
dashed rules (i.e., lines) in LaTeX. dashrule provides a
command, \hdashrule, which is a cross between LaTeX's \rule and
PostScript's setdash command. \hdashrule draws horizontally
dashed rules using the same syntax as \rule, but with an
additional, setdash-like parameter that specifies the pattern
of dash segments and the space between those segments. Because
dashrule's rules are constructed internally using \rule (as
opposed to, e.g., PostScript \specials) they are fully
compatible with every LaTeX back-end processor.

%package -n texlive-dashrule-doc
Summary:        Documentation for dashrule
Version:        svn29579.1.3

Provides:       tex-dashrule-doc
AutoReqProv:    No

%description -n texlive-dashrule-doc
Documentation for dashrule

%package -n texlive-dashundergaps
Provides:       tex-dashundergaps = %{tl_version}
License:        LPPL
Summary:        Underline with dotted or dashed lines
Version:        svn48081
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(ulem.sty)
Provides:       tex(dashundergaps.sty) = %{tl_version}

%description -n texlive-dashundergaps
The package provides commands (\underline, \dotuline and
\dashuline) each of which underlines its argument with one of
the styles the package is capable of. A phantom mode is
provided, where the underline (of whatever form) can serve for
a 'fill-in block' for student evaluation sheets.

%package -n texlive-dashundergaps-doc
Summary:        Documentation for dashundergaps
Version:        svn48081
Provides:       tex-dashundergaps-doc
AutoReqProv:    No

%description -n texlive-dashundergaps-doc
Documentation for dashundergaps

%package -n texlive-dataref
Provides:       tex-dataref = %{tl_version}
License:        LPPL 1.3
Summary:        Manage references to experimental data
Version:        svn42883
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pgf.sty), tex(kvoptions.sty), tex(xcolor.sty), tex(pdfcomment.sty)
Requires:       tex(xtab.sty), tex(booktabs.sty)
Provides:       tex(dataref.sty) = %{tl_version}

%description -n texlive-dataref
The package provides a mechanism that maintains a fixed
symbolic reference to numerical results; such results may vary
as the project proceeds (and hence the project report
develops).

%package -n texlive-dataref-doc
Summary:        Documentation for dataref
Version:        svn42883
Provides:       tex-dataref-doc
AutoReqProv:    No

%description -n texlive-dataref-doc
Documentation for dataref

%package -n texlive-datatool
Provides:       tex-datatool = %{tl_version}
License:        LPPL 1.3
Summary:        Tools to load and manipulate data
Version:        svn47543
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(datatool.sty), tex(tikz.sty), tex(etoolbox.sty)
Requires:       tex(mfirstuc.sty), tex(xfor.sty), tex(multicol.sty), tex(textcase.sty)
Requires:       tex(afterpage.sty), tex(amsmath.sty), tex(ifthen.sty), tex(substr.sty)
Requires:       tex(fp.sty), tex(pgfrcs.sty), tex(pgfkeys.sty), tex(pgfmath.sty)
Provides:       tex(databar.sty) = %{tl_version}, tex(databib.sty) = %{tl_version}
Provides:       tex(datagidx.sty) = %{tl_version}, tex(datapie.sty) = %{tl_version}
Provides:       tex(dataplot.sty) = %{tl_version}, tex(datatool-base.sty) = %{tl_version}
Provides:       tex(datatool-fp.sty) = %{tl_version}, tex(datatool-pgfmath.sty) = %{tl_version}
Provides:       tex(datatool.sty) = %{tl_version}, tex(person.sty) = %{tl_version}

%description -n texlive-datatool
The tools comprise six packages: datatool.sty: databases may be
created using LaTeX commands or by importing external files;
they may be sorted numerically or alphabetically; repetitive
operations (such as mail merging) may be performed on each row
of a database, subject to conditions to exclude particular
rows; commands are provided to examine database elements, and
to convert formats (for example, to convert a numeric element
to a format compatible with the fp package; datapie.sty: a
database may be represented as a pie chart; flexible options
allow colouring of the chart, and annotation hooks are
available; dataplot.sty: a database may be represented as a 2-
dimensional scatter or line plot; flexible options control of
the plot's overall appearance, and of legends and other extra
information; databar.sty: a database may be represented as a
bar chart; overall appearance, colouring and annotation are
controllable; datagidx.sty: provides a way of indexing or
creating glossaries/lists of acronyms that uses TeX to do the
sorting and collating instead of using an external indexing
application, such as xindy or makeindex; databib.sty: a
bibliography may be loaded into a datatool database, and
manipulated there before being printed (this permits a LaTeX-
based route to printing bibliographies in formats for which no
BibTeX style is available); and person.sty: provides support
for displaying a person's name and pronoun in a document, thus
avoiding cumbersome use of "he/she", etc. The drawing packages
make use of PGF/TikZ for their output. The bundle supersedes
and replaces the author's csvtools bundle.

%package -n texlive-datatool-doc
Summary:        Documentation for datatool
Version:        svn47543
Provides:       tex-datatool-doc
AutoReqProv:    No

%description -n texlive-datatool-doc
Documentation for datatool

%package -n texlive-dateiliste
Provides:       tex-dateiliste = %{tl_version}
License:        LPPL
Summary:        Extensions of the \listfiles concept
Version:        svn27974.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(svninfo.sty), tex(rcsinfo.sty), tex(ltxtable.sty)
Provides:       tex(dateiliste.sty) = %{tl_version}

%description -n texlive-dateiliste
The package provides a file list (similar to that offered by
\listfiles), neatly laid out as a table. The main document can
be included in the list, and a command is available for
providing RCS-maintained data for printing in the file list.

%package -n texlive-dateiliste-doc
Summary:        Documentation for dateiliste
Version:        svn27974.0.6

Provides:       tex-dateiliste-doc
AutoReqProv:    No

%description -n texlive-dateiliste-doc
Documentation for dateiliste

%package -n texlive-datenumber
Provides:       tex-datenumber = %{tl_version}
License:        LPPL
Summary:        Convert a date into a number and vice versa
Version:        svn18951.0.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(datenumber.sty) = %{tl_version}, tex(datenumberUSenglish.ldf) = %{tl_version}
Provides:       tex(datenumberdummy.ldf) = %{tl_version}
Provides:       tex(datenumberenglish.ldf) = %{tl_version}
Provides:       tex(datenumberfrench.ldf) = %{tl_version}
Provides:       tex(datenumbergerman.ldf) = %{tl_version}
Provides:       tex(datenumberspanish.ldf) = %{tl_version}

%description -n texlive-datenumber
This package provides commands to convert a date into a number
and vice versa. Additionally there are commands for
incrementing and decrementing a date. Leap years and the
Gregorian calendar reform are considered.

%package -n texlive-datenumber-doc
Summary:        Documentation for datenumber
Version:        svn18951.0.02

Provides:       tex-datenumber-doc
AutoReqProv:    No

%description -n texlive-datenumber-doc
Documentation for datenumber

%package -n texlive-datetime
Provides:       tex-datetime = %{tl_version}
License:        LPPL 1.3
Summary:        Change format of \today with commands for current time
Version:        svn36650.2.60

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(fmtcount.sty), tex(ifthen.sty)
Provides:       tex(datetime-defaults.sty) = %{tl_version}
Provides:       tex(datetime.sty) = %{tl_version}, tex(dt-UKenglish.def) = %{tl_version}
Provides:       tex(dt-USenglish.def) = %{tl_version}, tex(dt-american.def) = %{tl_version}
Provides:       tex(dt-australian.def) = %{tl_version}, tex(dt-austrian.def) = %{tl_version}
Provides:       tex(dt-bahasa.def) = %{tl_version}, tex(dt-basque.def) = %{tl_version}
Provides:       tex(dt-breton.def) = %{tl_version}, tex(dt-british.def) = %{tl_version}
Provides:       tex(dt-bulgarian.def) = %{tl_version}, tex(dt-canadian.def) = %{tl_version}
Provides:       tex(dt-catalan.def) = %{tl_version}, tex(dt-croatian.def) = %{tl_version}
Provides:       tex(dt-czech.def) = %{tl_version}, tex(dt-danish.def) = %{tl_version}
Provides:       tex(dt-dutch.def) = %{tl_version}, tex(dt-esperanto.def) = %{tl_version}
Provides:       tex(dt-estonian.def) = %{tl_version}, tex(dt-finnish.def) = %{tl_version}
Provides:       tex(dt-french.def) = %{tl_version}, tex(dt-galician.def) = %{tl_version}
Provides:       tex(dt-german.def) = %{tl_version}, tex(dt-greek.def) = %{tl_version}
Provides:       tex(dt-hebrew.def) = %{tl_version}, tex(dt-icelandic.def) = %{tl_version}
Provides:       tex(dt-irish.def) = %{tl_version}, tex(dt-italian.def) = %{tl_version}
Provides:       tex(dt-latin.def) = %{tl_version}, tex(dt-lsorbian.def) = %{tl_version}
Provides:       tex(dt-magyar.def) = %{tl_version}, tex(dt-naustrian.def) = %{tl_version}
Provides:       tex(dt-newzealand.def) = %{tl_version}, tex(dt-ngerman.def) = %{tl_version}
Provides:       tex(dt-norsk.def) = %{tl_version}, tex(dt-polish.def) = %{tl_version}
Provides:       tex(dt-portuges.def) = %{tl_version}, tex(dt-romanian.def) = %{tl_version}
Provides:       tex(dt-russian.def) = %{tl_version}, tex(dt-samin.def) = %{tl_version}
Provides:       tex(dt-scottish.def) = %{tl_version}, tex(dt-serbian.def) = %{tl_version}
Provides:       tex(dt-slovak.def) = %{tl_version}, tex(dt-slovene.def) = %{tl_version}
Provides:       tex(dt-spanish.def) = %{tl_version}, tex(dt-swedish.def) = %{tl_version}
Provides:       tex(dt-turkish.def) = %{tl_version}, tex(dt-ukraineb.def) = %{tl_version}
Provides:       tex(dt-usorbian.def) = %{tl_version}, tex(dt-welsh.def) = %{tl_version}

%description -n texlive-datetime
Provides various different formats for the text created by the
command \today, and also provides commands for displaying the
current time (or any given time), in 12-hour, 24-hour or text
format. The package overrides babel's date format, having its
own library of date formats in different languages. The package
requires the fmtcount package. This package is now obsolete and
has been replaced by datetime2.

%package -n texlive-datetime-doc
Summary:        Documentation for datetime
Version:        svn36650.2.60

Provides:       tex-datetime-doc
AutoReqProv:    No

%description -n texlive-datetime-doc
Documentation for datetime

%package -n texlive-datetime2
Provides:       tex-datetime2 = %{tl_version}
License:        LPPL 1.3
Summary:        Formats for dates, times and time zones
Version:        svn48236
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pgfkeys.sty), tex(pgfcalendar.sty), tex(tracklang.sty), tex(etoolbox.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(datetime2-calc.sty) = %{tl_version}, tex(datetime2.sty) = %{tl_version}

%description -n texlive-datetime2
This package provides commands for formatting dates, times and
time zones and redefines \today to use the same formatting
style. In addition to \today, you can also use \DTMcurrenttime
(current time) or \DTMnow (current date and time). Dates and
times can be saved for later use. The accompanying datetime2-
calc package can be used to convert date-times to UTC+00:00.
Language and regional support is provided by independently
maintained and installed modules. The datetime2-calc package
uses the pgfcalendar package (part of the PGF/TikZ bundle).
This package replaces datetime.sty which is now obsolete.

%package -n texlive-datetime2-doc
Summary:        Documentation for datetime2
Version:        svn48236
Provides:       tex-datetime2-doc
AutoReqProv:    No

%description -n texlive-datetime2-doc
Documentation for datetime2

%package -n texlive-datetime2-bahasai
Provides:       tex-datetime2-bahasai = %{tl_version}
License:        LPPL 1.3
Summary:        Bahasai language module for the datetime2 package
Version:        svn46287
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(datetime2-bahasai.ldf) = %{tl_version}

%description -n texlive-datetime2-bahasai
This module provides the "bahasai" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-bahasai-doc
Summary:        Documentation for datetime2-bahasai
Version:        svn46287
Provides:       tex-datetime2-bahasai-doc
AutoReqProv:    No

%description -n texlive-datetime2-bahasai-doc
Documentation for datetime2-bahasai

%package -n texlive-datetime2-basque
Provides:       tex-datetime2-basque = %{tl_version}
License:        LPPL 1.3
Summary:        Basque language module for the datetime2 package
Version:        svn47064
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(datetime2-basque.ldf) = %{tl_version}

%description -n texlive-datetime2-basque
This module provides the "basque" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-basque-doc
Summary:        Documentation for datetime2-basque
Version:        svn47064
Provides:       tex-datetime2-basque-doc
AutoReqProv:    No

%description -n texlive-datetime2-basque-doc
Documentation for datetime2-basque

%package -n texlive-datetime2-breton
Provides:       tex-datetime2-breton = %{tl_version}
License:        LPPL 1.3
Summary:        breton language module for the datetime2 package
Version:        svn47030
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-breton-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-breton-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-breton.ldf) = %{tl_version}

%description -n texlive-datetime2-breton
This module provides the "breton" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-breton-doc
Summary:        Documentation for datetime2-breton
Version:        svn47030
Provides:       tex-datetime2-breton-doc
AutoReqProv:    No

%description -n texlive-datetime2-breton-doc
Documentation for datetime2-breton

%package -n texlive-datetime2-bulgarian
Provides:       tex-datetime2-bulgarian = %{tl_version}
License:        LPPL 1.3
Summary:        Bulgarian language module for the datetime2 package
Version:        svn47031
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-bulgarian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-bulgarian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-bulgarian.ldf) = %{tl_version}

%description -n texlive-datetime2-bulgarian
This module provides the "bulgarian" style that can be set
using \DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-bulgarian-doc
Summary:        Documentation for datetime2-bulgarian
Version:        svn47031
Provides:       tex-datetime2-bulgarian-doc
AutoReqProv:    No

%description -n texlive-datetime2-bulgarian-doc
Documentation for datetime2-bulgarian

%package -n texlive-datetime2-catalan
Provides:       tex-datetime2-catalan = %{tl_version}
License:        LPPL 1.3
Summary:        catalan language module for the datetime2 package
Version:        svn47032
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-catalan-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-catalan-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-catalan.ldf) = %{tl_version}

%description -n texlive-datetime2-catalan
This module provides the "catalan" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-catalan-doc
Summary:        Documentation for datetime2-catalan
Version:        svn47032
Provides:       tex-datetime2-catalan-doc
AutoReqProv:    No

%description -n texlive-datetime2-catalan-doc
Documentation for datetime2-catalan

%package -n texlive-datetime2-croatian
Provides:       tex-datetime2-croatian = %{tl_version}
License:        LPPL 1.3
Summary:        croatian language module for the datetime2 package
Version:        svn36682.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-croatian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-croatian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-croatian.ldf) = %{tl_version}

%description -n texlive-datetime2-croatian
This module provides the "croatian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-croatian-doc
Summary:        Documentation for datetime2-croatian
Version:        svn36682.1.0

Provides:       tex-datetime2-croatian-doc
AutoReqProv:    No

%description -n texlive-datetime2-croatian-doc
Documentation for datetime2-croatian

%package -n texlive-datetime2-czech
Provides:       tex-datetime2-czech = %{tl_version}
License:        LPPL 1.3
Summary:        czech language module for the datetime2 package
Version:        svn47033
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-czech-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-czech-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-czech.ldf) = %{tl_version}

%description -n texlive-datetime2-czech
This module provides the "czech" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-czech-doc
Summary:        Documentation for datetime2-czech
Version:        svn47033
Provides:       tex-datetime2-czech-doc
AutoReqProv:    No

%description -n texlive-datetime2-czech-doc
Documentation for datetime2-czech

%package -n texlive-datetime2-danish
Provides:       tex-datetime2-danish = %{tl_version}
License:        LPPL 1.3
Summary:        danish language module for the datetime2 package
Version:        svn47034
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-danish-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-danish-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-danish.ldf) = %{tl_version}

%description -n texlive-datetime2-danish
This module provides the "danish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-danish-doc
Summary:        Documentation for datetime2-danish
Version:        svn47034
Provides:       tex-datetime2-danish-doc
AutoReqProv:    No

%description -n texlive-datetime2-danish-doc
Documentation for datetime2-danish

%package -n texlive-datetime2-dutch
Provides:       tex-datetime2-dutch = %{tl_version}
License:        LPPL 1.3
Summary:        dutch language module for the datetime2 package
Version:        svn47355
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(datetime2-dutch.ldf) = %{tl_version}

%description -n texlive-datetime2-dutch
This module provides the "dutch" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-dutch-doc
Summary:        Documentation for datetime2-dutch
Version:        svn47355
Provides:       tex-datetime2-dutch-doc
AutoReqProv:    No

%description -n texlive-datetime2-dutch-doc
Documentation for datetime2-dutch

%package -n texlive-datetime2-en-fulltext
Provides:       tex-datetime2-en-fulltext = %{tl_version}
License:        LPPL 1.3
Summary:        English Full Text styles for the datetime2 package
Version:        svn36705.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(datetime2.sty), tex(fmtcount.sty)
Provides:       tex(datetime2-en-fulltext.sty) = %{tl_version}

%description -n texlive-datetime2-en-fulltext
English date and time styles that use words for the numbers and
ordinals. This package provides the following date and time
styles: "en-fulltext", "en-FullText", "en-FULLTEXT", and the
additional time style "en-Fulltext". (The date equivalent can
be obtained through commands like \Today.) Unlike the base
styles provided by datetime2.sty, these styles aren't
expandable styles. This means that you can't use the date or
time in PDF bookmarks or in the argument of certain commands,
such as \MakeUppercase, while these styles are in use.

%package -n texlive-datetime2-en-fulltext-doc
Summary:        Documentation for datetime2-en-fulltext
Version:        svn36705.1.0

Provides:       tex-datetime2-en-fulltext-doc
AutoReqProv:    No

%description -n texlive-datetime2-en-fulltext-doc
Documentation for datetime2-en-fulltext

%package -n texlive-datetime2-english
Provides:       tex-datetime2-english = %{tl_version}
License:        LPPL 1.3
Summary:        English language module for the datetime2 package
Version:        svn39991

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(datetime2-en-AU.ldf) = %{tl_version}
Provides:       tex(datetime2-en-CA.ldf) = %{tl_version}
Provides:       tex(datetime2-en-GB.ldf) = %{tl_version}
Provides:       tex(datetime2-en-GG.ldf) = %{tl_version}
Provides:       tex(datetime2-en-IE.ldf) = %{tl_version}
Provides:       tex(datetime2-en-IM.ldf) = %{tl_version}
Provides:       tex(datetime2-en-JE.ldf) = %{tl_version}
Provides:       tex(datetime2-en-MT.ldf) = %{tl_version}
Provides:       tex(datetime2-en-NZ.ldf) = %{tl_version}
Provides:       tex(datetime2-en-US.ldf) = %{tl_version}
Provides:       tex(datetime2-english-base.ldf) = %{tl_version}
Provides:       tex(datetime2-english.ldf) = %{tl_version}

%description -n texlive-datetime2-english
This module provides the following styles that can be set using
\DTMsetstyle provided by datetime2.sty. The region not only
determines the date/time format but also the time zone
abbreviations if the zone mapping setting is on. english
(English - no region) en-GB (English - United Kingdom of Great
Britain and Northern Ireland) en-US (English - United States of
America) en-CA (English - Canada) en-AU (English - Commonwealth
of Australia) en-NZ (English - New Zealand) en-GG (English -
Bailiwick of Guernsey) en-JE (English - Bailiwick of Jersey) en-
IM (English - Isle of Man) en-MT (English - Republic of Malta)
en-IE (English - Republic of Ireland)

%package -n texlive-datetime2-english-doc
Summary:        Documentation for datetime2-english
Version:        svn39991

Provides:       tex-datetime2-english-doc
AutoReqProv:    No

%description -n texlive-datetime2-english-doc
Documentation for datetime2-english

%package -n texlive-datetime2-esperanto
Provides:       tex-datetime2-esperanto = %{tl_version}
License:        LPPL 1.3
Summary:        Esperanto language module for the datetime2 package
Version:        svn47356
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-esperanto-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-esperanto-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-esperanto.ldf) = %{tl_version}

%description -n texlive-datetime2-esperanto
This module provides the "esperanto" style that can be set
using \DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-esperanto-doc
Summary:        Documentation for datetime2-esperanto
Version:        svn47356
Provides:       tex-datetime2-esperanto-doc
AutoReqProv:    No

%description -n texlive-datetime2-esperanto-doc
Documentation for datetime2-esperanto

%package -n texlive-datetime2-estonian
Provides:       tex-datetime2-estonian = %{tl_version}
License:        LPPL 1.3
Summary:        Estonian language module for the datetime2 package
Version:        svn47565
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-estonian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-estonian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-estonian.ldf) = %{tl_version}

%description -n texlive-datetime2-estonian
This module provides the "estonian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-estonian-doc
Summary:        Documentation for datetime2-estonian
Version:        svn47565
Provides:       tex-datetime2-estonian-doc
AutoReqProv:    No

%description -n texlive-datetime2-estonian-doc
Documentation for datetime2-estonian

%package -n texlive-datetime2-finnish
Provides:       tex-datetime2-finnish = %{tl_version}
License:        LPPL 1.3
Summary:        Finnish language module for the datetime2 package
Version:        svn47047
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-finnish-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-finnish-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-finnish.ldf) = %{tl_version}

%description -n texlive-datetime2-finnish
This module provides the "finnish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-finnish-doc
Summary:        Documentation for datetime2-finnish
Version:        svn47047
Provides:       tex-datetime2-finnish-doc
AutoReqProv:    No

%description -n texlive-datetime2-finnish-doc
Documentation for datetime2-finnish

%package -n texlive-datetime2-french
Provides:       tex-datetime2-french = %{tl_version}
License:        LPPL 1.3
Summary:        French language module for the datetime2 package
Version:        svn43742
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-french-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-french-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-french.ldf) = %{tl_version}

%description -n texlive-datetime2-french
This module provides the "french" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-french-doc
Summary:        Documentation for datetime2-french
Version:        svn43742
Provides:       tex-datetime2-french-doc
AutoReqProv:    No

%description -n texlive-datetime2-french-doc
Documentation for datetime2-french

%package -n texlive-datetime2-galician
Provides:       tex-datetime2-galician = %{tl_version}
License:        LPPL 1.3
Summary:        galician language module for the datetime2 package
Version:        svn47631
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-galician-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-galician-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-galician.ldf) = %{tl_version}

%description -n texlive-datetime2-galician
This module provides the "galician" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-galician-doc
Summary:        Documentation for datetime2-galician
Version:        svn47631
Provides:       tex-datetime2-galician-doc
AutoReqProv:    No

%description -n texlive-datetime2-galician-doc
Documentation for datetime2-galician

%package -n texlive-datetime2-german
Provides:       tex-datetime2-german = %{tl_version}
License:        LPPL 1.3
Summary:        German language module for the datetime2 package
Version:        svn45800
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-german-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-german-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-german.ldf) = %{tl_version}

%description -n texlive-datetime2-german
This module provides the "german" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-german-doc
Summary:        Documentation for datetime2-german
Version:        svn45800
Provides:       tex-datetime2-german-doc
AutoReqProv:    No

%description -n texlive-datetime2-german-doc
Documentation for datetime2-german

%package -n texlive-datetime2-greek
Provides:       tex-datetime2-greek = %{tl_version}
License:        LPPL 1.3
Summary:        Greek language module for the datetime2 package
Version:        svn47533
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-greek-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-greek-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-greek.ldf) = %{tl_version}

%description -n texlive-datetime2-greek
This module provides the "greek" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-greek-doc
Summary:        Documentation for datetime2-greek
Version:        svn47533
Provides:       tex-datetime2-greek-doc
AutoReqProv:    No

%description -n texlive-datetime2-greek-doc
Documentation for datetime2-greek

%package -n texlive-datetime2-hebrew
Provides:       tex-datetime2-hebrew = %{tl_version}
License:        LPPL 1.3
Summary:        Hebrew language module for the datetime2 package
Version:        svn47534
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(datetime2-hebrew.ldf) = %{tl_version}

%description -n texlive-datetime2-hebrew
This module provides the "hebrew" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-hebrew-doc
Summary:        Documentation for datetime2-hebrew
Version:        svn47534
Provides:       tex-datetime2-hebrew-doc
AutoReqProv:    No

%description -n texlive-datetime2-hebrew-doc
Documentation for datetime2-hebrew

%package -n texlive-datetime2-icelandic
Provides:       tex-datetime2-icelandic = %{tl_version}
License:        LPPL 1.3
Summary:        Icelandic language module for the datetime2 package
Version:        svn47501
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-icelandic-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-icelandic-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-icelandic.ldf) = %{tl_version}

%description -n texlive-datetime2-icelandic
This module provides the "icelandic" style that can be set
using \DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-icelandic-doc
Summary:        Documentation for datetime2-icelandic
Version:        svn47501
Provides:       tex-datetime2-icelandic-doc
AutoReqProv:    No

%description -n texlive-datetime2-icelandic-doc
Documentation for datetime2-icelandic

%package -n texlive-datetime2-irish
Provides:       tex-datetime2-irish = %{tl_version}
License:        LPPL 1.3
Summary:        Irish Gaelic Language Module for the datetime2 Package
Version:        svn47632
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-ga-GB.ldf) = %{tl_version}
Provides:       tex(datetime2-ga-IE.ldf) = %{tl_version}
Provides:       tex(datetime2-irish-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-irish-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-irish.ldf) = %{tl_version}

%description -n texlive-datetime2-irish
This module provides the "irish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-irish-doc
Summary:        Documentation for datetime2-irish
Version:        svn47632
Provides:       tex-datetime2-irish-doc
AutoReqProv:    No

%description -n texlive-datetime2-irish-doc
Documentation for datetime2-irish

%package -n texlive-datetime2-italian
Provides:       tex-datetime2-italian = %{tl_version}
License:        LPPL 1.3
Summary:        Italian language module for the datetime2 package
Version:        svn37146.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-italian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-italian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-italian.ldf) = %{tl_version}

%description -n texlive-datetime2-italian
This module provides the "italian" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-italian-doc
Summary:        Documentation for datetime2-italian
Version:        svn37146.1.3

Provides:       tex-datetime2-italian-doc
AutoReqProv:    No

%description -n texlive-datetime2-italian-doc
Documentation for datetime2-italian

%package -n texlive-datetime2-it-fulltext
Provides:       tex-datetime2-it-fulltext = %{tl_version}
License:        LPPL 1.3
Summary:        Italian full text styles for the datetime2 package
Version:        svn38093.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(datetime2.sty), tex(itnumpar.sty), tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-it-fulltext-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-it-fulltext-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-it-fulltext.sty) = %{tl_version}

%description -n texlive-datetime2-it-fulltext
Italian date and time styles that use words for the numbers and
ordinals. This package provides the following date and time
styles: "it-fulltext" and "it-fulltext-twenty-four". The first
style uses a format "am pm", the second a format "24 hours".
The necessary packages are datetime2, itnumpar, ifxetex, and
ifluatex. This package is the translation and adaptation of
datetime2-en-fulltext.

%package -n texlive-datetime2-it-fulltext-doc
Summary:        Documentation for datetime2-it-fulltext
Version:        svn38093.1.6

Provides:       tex-datetime2-it-fulltext-doc
AutoReqProv:    No

%description -n texlive-datetime2-it-fulltext-doc
Documentation for datetime2-it-fulltext

%package -n texlive-datetime2-latin
Provides:       tex-datetime2-latin = %{tl_version}
License:        LPPL 1.3
Summary:        Latin language module for the datetime2 package
Version:        svn47748
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(datetime2-latin.ldf) = %{tl_version}

%description -n texlive-datetime2-latin
This module provides the "latin" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-latin-doc
Summary:        Documentation for datetime2-latin
Version:        svn47748
Provides:       tex-datetime2-latin-doc
AutoReqProv:    No

%description -n texlive-datetime2-latin-doc
Documentation for datetime2-latin

%package -n texlive-datetime2-lsorbian
Provides:       tex-datetime2-lsorbian = %{tl_version}
License:        LPPL 1.3
Summary:        Lower Sorbian language module for the datetime2 package
Version:        svn47749
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-lsorbian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-lsorbian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-lsorbian.ldf) = %{tl_version}

%description -n texlive-datetime2-lsorbian
This module provides the "lsorbian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-lsorbian-doc
Summary:        Documentation for datetime2-lsorbian
Version:        svn47749
Provides:       tex-datetime2-lsorbian-doc
AutoReqProv:    No

%description -n texlive-datetime2-lsorbian-doc
Documentation for datetime2-lsorbian

%package -n texlive-datetime2-magyar
Provides:       tex-datetime2-magyar = %{tl_version}
License:        LPPL 1.3
Summary:        magyar language module for the datetime2 package
Version:        svn48266
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-magyar-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-magyar-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-magyar.ldf) = %{tl_version}

%description -n texlive-datetime2-magyar
This module provides the "magyar" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-magyar-doc
Summary:        Documentation for datetime2-magyar
Version:        svn48266
Provides:       tex-datetime2-magyar-doc
AutoReqProv:    No

%description -n texlive-datetime2-magyar-doc
Documentation for datetime2-magyar

%package -n texlive-datetime2-norsk
Provides:       tex-datetime2-norsk = %{tl_version}
License:        LPPL 1.3
Summary:        Norsk language module for the datetime2 package
Version:        svn48267
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-norsk-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-norsk-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-norsk.ldf) = %{tl_version}

%description -n texlive-datetime2-norsk
This module provides the "norsk" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-norsk-doc
Summary:        Documentation for datetime2-norsk
Version:        svn48267
Provides:       tex-datetime2-norsk-doc
AutoReqProv:    No

%description -n texlive-datetime2-norsk-doc
Documentation for datetime2-norsk

%package -n texlive-datetime2-polish
Provides:       tex-datetime2-polish = %{tl_version}
License:        LPPL 1.3
Summary:        polish language module for the datetime2 package
Version:        svn36692.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-polish-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-polish-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-polish.ldf) = %{tl_version}

%description -n texlive-datetime2-polish
This module provides the "polish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-polish-doc
Summary:        Documentation for datetime2-polish
Version:        svn36692.1.0

Provides:       tex-datetime2-polish-doc
AutoReqProv:    No

%description -n texlive-datetime2-polish-doc
Documentation for datetime2-polish

%package -n texlive-datetime2-portuges
Provides:       tex-datetime2-portuges = %{tl_version}
License:        LPPL 1.3
Summary:        Portuguese language module for the datetime2 package
Version:        svn36670.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-portuges-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-portuges-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-portuges.ldf) = %{tl_version}

%description -n texlive-datetime2-portuges
This module provides the "portuges" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-portuges-doc
Summary:        Documentation for datetime2-portuges
Version:        svn36670.1.0

Provides:       tex-datetime2-portuges-doc
AutoReqProv:    No

%description -n texlive-datetime2-portuges-doc
Documentation for datetime2-portuges

%package -n texlive-datetime2-romanian
Provides:       tex-datetime2-romanian = %{tl_version}
License:        LPPL 1.3
Summary:        Romanian language module for the datetime2 package
Version:        svn43743
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-romanian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-romanian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-romanian.ldf) = %{tl_version}

%description -n texlive-datetime2-romanian
This module provides the "romanian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-romanian-doc
Summary:        Documentation for datetime2-romanian
Version:        svn43743
Provides:       tex-datetime2-romanian-doc
AutoReqProv:    No

%description -n texlive-datetime2-romanian-doc
Documentation for datetime2-romanian

%package -n texlive-datetime2-russian
Provides:       tex-datetime2-russian = %{tl_version}
License:        LPPL 1.3
Summary:        russian language module for the datetime2 package
Version:        svn36692.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-russian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-russian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-russian.ldf) = %{tl_version}

%description -n texlive-datetime2-russian
This module provides the "russian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-russian-doc
Summary:        Documentation for datetime2-russian
Version:        svn36692.1.0

Provides:       tex-datetime2-russian-doc
AutoReqProv:    No

%description -n texlive-datetime2-russian-doc
Documentation for datetime2-russian

%package -n texlive-datetime2-samin
Provides:       tex-datetime2-samin = %{tl_version}
License:        LPPL 1.3
Summary:        Northern Sami language module for the datetime2 package
Version:        svn36692.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-samin-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-samin-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-samin.ldf) = %{tl_version}

%description -n texlive-datetime2-samin
This module provides the "samin" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-samin-doc
Summary:        Documentation for datetime2-samin
Version:        svn36692.1.0

Provides:       tex-datetime2-samin-doc
AutoReqProv:    No

%description -n texlive-datetime2-samin-doc
Documentation for datetime2-samin

%package -n texlive-datetime2-scottish
Provides:       tex-datetime2-scottish = %{tl_version}
License:        LPPL 1.3
Summary:        Scottish Gaelic Language Module for the datetime2 Package
Version:        svn36625.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-scottish-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-scottish-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-scottish.ldf) = %{tl_version}

%description -n texlive-datetime2-scottish
This module provides the "scottish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-scottish-doc
Summary:        Documentation for datetime2-scottish
Version:        svn36625.1.0

Provides:       tex-datetime2-scottish-doc
AutoReqProv:    No

%description -n texlive-datetime2-scottish-doc
Documentation for datetime2-scottish

%package -n texlive-datetime2-serbian
Provides:       tex-datetime2-serbian = %{tl_version}
License:        LPPL 1.3
Summary:        serbian language module for the datetime2 package
Version:        svn36699.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-serbian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-serbian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-serbian.ldf) = %{tl_version}

%description -n texlive-datetime2-serbian
This module provides the "serbian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-serbian-doc
Summary:        Documentation for datetime2-serbian
Version:        svn36699.1.0

Provides:       tex-datetime2-serbian-doc
AutoReqProv:    No

%description -n texlive-datetime2-serbian-doc
Documentation for datetime2-serbian

%package -n texlive-datetime2-slovak
Provides:       tex-datetime2-slovak = %{tl_version}
License:        LPPL 1.3
Summary:        slovak language module for the datetime2 package
Version:        svn36700.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-slovak-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-slovak-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-slovak.ldf) = %{tl_version}

%description -n texlive-datetime2-slovak
This module provides the "slovak" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-slovak-doc
Summary:        Documentation for datetime2-slovak
Version:        svn36700.1.0

Provides:       tex-datetime2-slovak-doc
AutoReqProv:    No

%description -n texlive-datetime2-slovak-doc
Documentation for datetime2-slovak

%package -n texlive-datetime2-slovene
Provides:       tex-datetime2-slovene = %{tl_version}
License:        LPPL 1.3
Summary:        slovene language module for the datetime2 package
Version:        svn36700.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-slovene-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-slovene-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-slovene.ldf) = %{tl_version}

%description -n texlive-datetime2-slovene
This module provides the "slovene" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-slovene-doc
Summary:        Documentation for datetime2-slovene
Version:        svn36700.1.0

Provides:       tex-datetime2-slovene-doc
AutoReqProv:    No

%description -n texlive-datetime2-slovene-doc
Documentation for datetime2-slovene

%package -n texlive-datetime2-spanish
Provides:       tex-datetime2-spanish = %{tl_version}
License:        LPPL 1.3
Summary:        Spanish language module for the datetime2 package
Version:        svn45785
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-spanish-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-spanish-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-spanish.ldf) = %{tl_version}

%description -n texlive-datetime2-spanish
This module provides the "spanish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-spanish-doc
Summary:        Documentation for datetime2-spanish
Version:        svn45785
Provides:       tex-datetime2-spanish-doc
AutoReqProv:    No

%description -n texlive-datetime2-spanish-doc
Documentation for datetime2-spanish

%package -n texlive-datetime2-swedish
Provides:       tex-datetime2-swedish = %{tl_version}
License:        LPPL 1.3
Summary:        swedish language module for the datetime2 package
Version:        svn36700.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-swedish-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-swedish-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-swedish.ldf) = %{tl_version}

%description -n texlive-datetime2-swedish
This module provides the "swedish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-swedish-doc
Summary:        Documentation for datetime2-swedish
Version:        svn36700.1.0

Provides:       tex-datetime2-swedish-doc
AutoReqProv:    No

%description -n texlive-datetime2-swedish-doc
Documentation for datetime2-swedish

%package -n texlive-datetime2-turkish
Provides:       tex-datetime2-turkish = %{tl_version}
License:        LPPL 1.3
Summary:        turkish language module for the datetime2 package
Version:        svn36700.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-turkish-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-turkish-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-turkish.ldf) = %{tl_version}

%description -n texlive-datetime2-turkish
This module provides the "turkish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-turkish-doc
Summary:        Documentation for datetime2-turkish
Version:        svn36700.1.0

Provides:       tex-datetime2-turkish-doc
AutoReqProv:    No

%description -n texlive-datetime2-turkish-doc
Documentation for datetime2-turkish

%package -n texlive-datetime2-ukrainian
Provides:       tex-datetime2-ukrainian = %{tl_version}
License:        LPPL 1.3
Summary:        Ukrainian language module for the datetime2 package
Version:        svn47552
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-ukrainian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-ukrainian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-ukrainian.ldf) = %{tl_version}

%description -n texlive-datetime2-ukrainian
This module provides the "ukrainian" style that can be set
using \DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-ukrainian-doc
Summary:        Documentation for datetime2-ukrainian
Version:        svn47552
Provides:       tex-datetime2-ukrainian-doc
AutoReqProv:    No

%description -n texlive-datetime2-ukrainian-doc
Documentation for datetime2-ukrainian

%package -n texlive-datetime2-usorbian
Provides:       tex-datetime2-usorbian = %{tl_version}
License:        LPPL 1.3
Summary:        Upper Sorbian language module for the datetime2 package
Version:        svn36700.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-usorbian-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-usorbian-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-usorbian.ldf) = %{tl_version}

%description -n texlive-datetime2-usorbian
This module provides the "usorbian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-usorbian-doc
Summary:        Documentation for datetime2-usorbian
Version:        svn36700.1.0

Provides:       tex-datetime2-usorbian-doc
AutoReqProv:    No

%description -n texlive-datetime2-usorbian-doc
Documentation for datetime2-usorbian

%package -n texlive-datetime2-welsh
Provides:       tex-datetime2-welsh = %{tl_version}
License:        LPPL 1.3
Summary:        Welsh language module for the datetime2 package
Version:        svn36636.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(ifluatex.sty)
Provides:       tex(datetime2-welsh-ascii.ldf) = %{tl_version}
Provides:       tex(datetime2-welsh-utf8.ldf) = %{tl_version}
Provides:       tex(datetime2-welsh.ldf) = %{tl_version}

%description -n texlive-datetime2-welsh
This module provides the "welsh" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-welsh-doc
Summary:        Documentation for datetime2-welsh
Version:        svn36636.1.0

Provides:       tex-datetime2-welsh-doc
AutoReqProv:    No

%description -n texlive-datetime2-welsh-doc
Documentation for datetime2-welsh

%package -n texlive-dblfloatfix
Provides:       tex-dblfloatfix = %{tl_version}
License:        LPPL 1.3
Summary:        Fixes for twocolumn floats
Version:        svn28983.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fixltx2e.sty)
Provides:       tex(dblfloatfix.sty) = %{tl_version}

%description -n texlive-dblfloatfix
The package solves two problems: floats in a twocolumn document
come out in the right order and allowed float positions are now
[tbp]. The package actually merges facilities from fixltx2e and
stfloats.

%package -n texlive-dblfloatfix-doc
Summary:        Documentation for dblfloatfix
Version:        svn28983.1.0a

Provides:       tex-dblfloatfix-doc
AutoReqProv:    No

%description -n texlive-dblfloatfix-doc
Documentation for dblfloatfix

%package -n texlive-decimal
Provides:       tex-decimal = %{tl_version}
License:        LPPL
Summary:        LaTeX package for the English raised decimal point
Version:        svn23374.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(decimal.sty) = %{tl_version}

%description -n texlive-decimal
This LaTeX package should be used by people who need the
traditional English raised decimal point, instead of the
American-style period.

%package -n texlive-decimal-doc
Summary:        Documentation for decimal
Version:        svn23374.0

Provides:       tex-decimal-doc
AutoReqProv:    No

%description -n texlive-decimal-doc
Documentation for decimal

%package -n texlive-decorule
Provides:       tex-decorule = %{tl_version}
License:        LPPL 1.3
Summary:        Decorative swelled rule using font character
Version:        svn23487.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(fix-cm.sty)
Provides:       tex(decorule.sty) = %{tl_version}

%description -n texlive-decorule
The package implements a decorative swelled rule using only a
symbol from a font installed with all distributions of TeX, so
it works independently, without the need to install any
additional software or fonts. This is the packaged version of
the macro which was originally published in the "Typographers'
Inn" column in TUGboat 31:1 (2010).

%package -n texlive-decorule-doc
Summary:        Documentation for decorule
Version:        svn23487.0.6

Provides:       tex-decorule-doc
AutoReqProv:    No

%description -n texlive-decorule-doc
Documentation for decorule

%package -n texlive-delim
Provides:       tex-delim = %{tl_version}
License:        LPPL 1.2
Summary:        Simplify typesetting mathematical delimiters
Version:        svn23974.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(delim.sty) = %{tl_version}

%description -n texlive-delim
The package permits simpler control of delimiters without
excessive use of \big... commands (and the like).

%package -n texlive-delim-doc
Summary:        Documentation for delim
Version:        svn23974.1.0

Provides:       tex-delim-doc
AutoReqProv:    No

%description -n texlive-delim-doc
Documentation for delim

%package -n texlive-delimtxt
Provides:       tex-delimtxt = %{tl_version}
License:        LPPL
Summary:        Read and parse text tables
Version:        svn16549.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(delimtxt.sty) = %{tl_version}

%description -n texlive-delimtxt
This experimental package can read and parse text tables
delimited by user-defined tokens (e.g., tab). It can be used
for serial letters and the like, making it easier to export the
data file from MS-Excel/MS-Word

%package -n texlive-delimtxt-doc
Summary:        Documentation for delimtxt
Version:        svn16549.0

Provides:       tex-delimtxt-doc
AutoReqProv:    No

%description -n texlive-delimtxt-doc
Documentation for delimtxt

%package -n texlive-denisbdoc
Provides:       tex-denisbdoc = %{tl_version}
License:        LPPL 1.3
Summary:        A personal dirty package for documenting packages
Version:        svn42829
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(l3keys2e.sty), tex(xparse.sty), tex(fontenc.sty)
Requires:       tex(inputenc.sty), tex(fontspec.sty), tex(xpatch.sty), tex(morewrites.sty)
Requires:       tex(parskip.sty), tex(amsthm.sty), tex(thmtools.sty), tex(fixfoot.sty)
Requires:       tex(enumitem.sty), tex(afterpage.sty), tex(tabulary.sty), tex(calc.sty)
Requires:       tex(siunitx.sty), tex(tocbibind.sty), tex(varioref.sty), tex(booktabs.sty)
Requires:       tex(zref.sty), tex(footmisc.sty), tex(rotating.sty), tex(pdflscape.sty)
Requires:       tex(hologo.sty), tex(xifthen.sty), tex(refcount.sty), tex(iflang.sty)
Requires:       tex(amssymb.sty), tex(tocvsec2.sty), tex(csquotes.sty), tex(tikz.sty)
Requires:       tex(imakeidx.sty), tex(tcolorbox.sty), tex(comment.sty), tex(path.sty)
Requires:       tex(textcase.sty), tex(biblatex.sty), tex(babel.sty), tex(menukeys.sty)
Requires:       tex(datetime.sty), tex(hyperref.sty), tex(nameref.sty), tex(hypcap.sty)
Requires:       tex(bookmark.sty), tex(glossaries.sty), tex(cleveref.sty)
Provides:       tex(denisbdoc.sty) = %{tl_version}

%description -n texlive-denisbdoc
A personal dirty package for documenting packages.

%package -n texlive-denisbdoc-doc
Summary:        Documentation for denisbdoc
Version:        svn42829
Provides:       tex-denisbdoc-doc
AutoReqProv:    No

%description -n texlive-denisbdoc-doc
Documentation for denisbdoc

%package -n texlive-dccpaper
Provides:       tex-dccpaper = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset papers for the International Journal of Digital Curation
Version:        svn47717
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(dccpaper-base.tex) = %{tl_version}, tex(idcc.cls) = %{tl_version}
Provides:       tex(ijdc-v9.cls) = %{tl_version}

%description -n texlive-dccpaper
The LaTeX class ijdc-v9 produces camera-ready papers and
articles suitable for inclusion in the International Journal of
Digital Curation, with applicability from volume 9 onwards. The
similar idcc class can be used for submissions to the
International Digital Curation Conference, beginning with the
2015 conference.

%package -n texlive-dccpaper-doc
Summary:        Documentation for dccpaper
Version:        svn47717
Provides:       tex-dccpaper-doc
AutoReqProv:    No

%description -n texlive-dccpaper-doc
Documentation for dccpaper

%package -n texlive-cryptocode
Provides:       tex-cryptocode = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting pseudocode, protocols, game-based proofs and black-box reductions in cryptography
Version:        svn37019.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(mathtools.sty), tex(amsfonts.sty), tex(xcolor.sty)
Requires:       tex(calc.sty), tex(tikz.sty), tex(ifthen.sty), tex(xargs.sty)
Requires:       tex(pgf.sty), tex(forloop.sty), tex(array.sty), tex(xparse.sty)
Requires:       tex(l3regex.sty), tex(pbox.sty), tex(varwidth.sty), tex(suffix.sty)
Requires:       tex(etoolbox.sty), tex(etex.sty), tex(environ.sty), tex(xkeyval.sty)
Provides:       tex(cryptocode.sty) = %{tl_version}

%description -n texlive-cryptocode
The cryptocode bundle provides commands for easily typesetting
pseudocode and simple protocols as well as environments for
visualizing game-based proofs and black-box reductions as often
used within the cryptographic community.

%package -n texlive-cryptocode-doc
Summary:        Documentation for cryptocode
Version:        svn37019.0.1

Provides:       tex-cryptocode-doc
AutoReqProv:    No

%description -n texlive-cryptocode-doc
Documentation for cryptocode

%package -n texlive-cquthesis-doc
Provides:       tex-cquthesis-doc = %{tl_version}
License:        LPPL
Summary:        doc files of cquthesis
Version:        svn46863
AutoReqProv:    No

%description -n texlive-cquthesis-doc
Documentation for cquthesis

%package -n texlive-cquthesis
Provides:       tex-cquthesis = %{tl_version}
License:        LPPL
Summary:        LaTeX Thesis Template for Chongqing University
Version:        svn46863
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(cquthesis.cls) = %{tl_version}, tex(cquthesis.sty) = %{tl_version}
Provides:       tex(cquthesis.cfg) = %{tl_version}

%description -n texlive-cquthesis
CQUThesis stands for Chongqing University Thesis Template for
LaTeX, bearing the ability to support bachelor, master, doctor
dissertations with grace and speed.

%package -n texlive-crimson-doc
Provides:       tex-crimson-doc = %{tl_version}
License:        LPPL and OFL
Summary:        doc files of crimson
Version:        svn43525
AutoReqProv:    No

%description -n texlive-crimson-doc
Documentation for crimson

%package -n texlive-crimson
Provides:       tex-crimson = %{tl_version}
License:        LPPL and OFL
Summary:        Crimson fonts with LaTeX support
Version:        svn43525
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(crimson.sty) = %{tl_version}, tex(crimson.map) = %{tl_version}
Provides:       tex(OT1Crimson-TLF.fd) = %{tl_version}, tex(LY1Crimson-TLF.fd) = %{tl_version}
Provides:       tex(TS1Crimson-TLF.fd) = %{tl_version}, tex(T1Crimson-TLF.fd) = %{tl_version}
Provides:       tex(Crimson-Italic.pfb) = %{tl_version}, tex(Crimson-Bold.pfb) = %{tl_version}
Provides:       tex(Crimson-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Crimson-Roman.pfb) = %{tl_version}, tex(Crimson-SemiboldItalic.pfb) = %{tl_version}
Provides:       tex(Crimson-Semibold.pfb) = %{tl_version}
Provides:       tex(crm_izufyi.enc) = %{tl_version}, tex(crm_wsbs26.enc) = %{tl_version}
Provides:       tex(crm_ue2axx.enc) = %{tl_version}, tex(crm_jdlmpi.enc) = %{tl_version}
Provides:       tex(crm_axwm4k.enc) = %{tl_version}, tex(crm_fllea6.enc) = %{tl_version}
Provides:       tex(crm_wef5am.enc) = %{tl_version}, tex(crm_g4bzis.enc) = %{tl_version}
Provides:       tex(crm_odbuza.enc) = %{tl_version}, tex(crm_bchha2.enc) = %{tl_version}
Provides:       tex(crm_ayvnmf.enc) = %{tl_version}, tex(crm_wttfgh.enc) = %{tl_version}
Provides:       tex(crm_uafi7a.enc) = %{tl_version}, tex(crm_n3gbj7.enc) = %{tl_version}
Provides:       tex(crm_vcz7kx.enc) = %{tl_version}, tex(crm_qrsm2e.enc) = %{tl_version}
Provides:       tex(crm_kwsa5r.enc) = %{tl_version}, tex(crm_qst7o4.enc) = %{tl_version}
Provides:       tex(crm_ory2k7.enc) = %{tl_version}, tex(crm_tyw3ea.enc) = %{tl_version}
Provides:       tex(crm_3bejww.enc) = %{tl_version}, tex(crm_myjoho.enc) = %{tl_version}
Provides:       tex(Crimson-Italic.otf) = %{tl_version}, tex(Crimson-Roman.otf) = %{tl_version}
Provides:       tex(Crimson-Semibold.otf) = %{tl_version}
Provides:       tex(Crimson-Bold.otf) = %{tl_version}, tex(Crimson-SemiboldItalic.otf) = %{tl_version}
Provides:       tex(Crimson-BoldItalic.otf) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Crimson-Roman-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Crimson-Roman-tlf-t1.vf) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Crimson-Roman-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Crimson-Roman-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-Roman-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Crimson-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-SemiboldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Crimson-Roman-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-Roman-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Crimson-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Crimson-Semibold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Crimson-Roman-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Crimson-Italic-tlf-ts1--base.tfm) = %{tl_version}

%description -n texlive-crimson
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX
support for the Crimson family of fonts, designed by Sebastian
Kosch. The Crimson family is for book production in the
tradition of beautiful oldstyle typefaces, inspired
particularly by the work of people like Jan Tschichold (Sabon),
Robert Slimbach (Arno, Minion), and Jonathan Hoefler (Hoefler
Text). Support for small caps and old-style numerals is still
"under construction"; these features are not supported by this
version of the package.

%package -n texlive-ctablestack-doc
Provides:       tex-ctablestack-doc = %{tl_version}
License:        LPPL
Summary:        doc files of ctablestack
Version:        svn38514

AutoReqProv:    No

%description -n texlive-ctablestack-doc
Documentation for ctablestack

%package -n texlive-ctablestack
Provides:       tex-ctablestack = %{tl_version}
License:        LPPL
Summary:        Catcode table stable support
Version:        svn38514

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ctablestack.sty) = %{tl_version}

%description -n texlive-ctablestack
This package provides a method for defining category code table
stacks in LuaTeX. It builds on code provided by the 2015/10/01
release of LaTeX2e (also available as ltluatex.sty for plain
users). It is required by the luatexbase package (v1.0 onward)
which uses ctablestack to provide a back-compatibility form of
this concept.

%package -n texlive-delimseasy-doc
Provides:       tex-delimseasy-doc = %{tl_version}
License:        LPPL
Summary:        doc files of delimseasy
Version:        svn39589

AutoReqProv:    No

%description -n texlive-delimseasy-doc
Documentation for delimseasy

%package -n texlive-delimseasy
Provides:       tex-delimseasy = %{tl_version}
License:        LPPL
Summary:        Delimiter commands that are easy to use and resize
Version:        svn39589

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(delimseasy.sty) = %{tl_version}

%description -n texlive-delimseasy
This package provides commands to give a consistent, easy-to-
remember, easy to edit way to control the size and blackness of
delimiters: append 1-4 "b"s to command for larger sizes;
prepend "B" for for boldface. These commands reduce the
likelihood of incomplete delimeter pairs and typically use
fewer characters than the LaTeX default.

%package -n texlive-crossreftools
Summary:        Expandable extraction of cleveref data
Version:        svn47012
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(crossreftools.sty) = %{tl_version}

%description -n texlive-crossreftools
The package provides expandable extraction of information
stored in labels generated with cleveref.

%package -n texlive-css-colors
Summary:        Named colors for web-safe design
Version:        svn43961
License:        LPPL and GPL+
Requires:       texlive-base texlive-kpathsea
Provides:       tex(css-colors.sty) = %{tl_version}

%description -n texlive-css-colors
This package defines web-safe colors for use with D.P.
Carlisle's color package. It is intended for both authors and
package writers (e.g. to create Beamer color themes).

%package -n texlive-cstypo
Summary:        Czech typography rules enforced through LuaTeX hooks
Version:        svn41986
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cstypo.sty) = %{tl_version}, tex(cstypo-tex.tex) = %{tl_version}

%description -n texlive-cstypo
This package provides macros that enforce basic Czech
typography rules through Lua hooks available in LuaTeX.

%package -n texlive-currency
Summary:        Format currencies in a consistent way
Version:        svn44489
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(currency.sty) = %{tl_version}

%description -n texlive-currency
The package facilitates the formatting of currencies (amounts
and units) with various formatting capabilities.

%package -n texlive-cqubeamer
Summary:        LaTeX Beamer Template for Chongqing University
Version:        svn47630
License:        MIT and CC-BY
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cqubeamer.sty) = %{tl_version}

%description -n texlive-cqubeamer
This package provides a LaTeX beamer template designed for
researchers of Chongqing University. It can be used for
academic reports, conferences, or thesis defense, and can be
helpful for delivering a speech. It should be used with the
XeTeX engine.

%package -n texlive-dejavu-otf
Summary:        Support for the ttf and otf DejaVu fonts
Version:        svn45991
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(dejavu-otf.sty) = %{tl_version}

%description -n texlive-dejavu-otf
Package dejavu-otf supports the free ttf-fonts from the DejaVu
project which are available from GitHub or already part of your
system (Windows/Linux/...) and the OpenType version of the
TeXGyre Math, which is part of any TeX distribution.

%package -n texlive-delimset
Summary:        Typeset and declare sets of delimiters with convenient size control
Version:        svn46359
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(delimset.sty) = %{tl_version}

%description -n texlive-delimset
delimset is a LaTeX2e package to typeset and declare sets of
delimiters in math mode whose size can be adjusted
conveniently.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD

cd %{buildroot}%{_texdir}/texmf-dist/

install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/cyklop public/dantelogo"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-custom-bib
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/custom-bib/

%files -n texlive-custom-bib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/custom-bib/

%files -n texlive-ctan_chk-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/support/ctan_chk/

%files -n texlive-cryst
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/cryst/
%{_texdir}/texmf-dist/fonts/source/public/cryst/
%{_texdir}/texmf-dist/fonts/tfm/public/cryst/
%{_texdir}/texmf-dist/fonts/type1/public/cryst/

%files -n texlive-cryst-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cryst/

%files -n texlive-cyklop
%license gfl.txt
%{_datadir}/fonts/cyklop
%{_texdir}/texmf-dist/fonts/afm/public/cyklop/
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/
%{_texdir}/texmf-dist/fonts/map/dvips/cyklop/
%{_texdir}/texmf-dist/fonts/opentype/public/cyklop/
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/
%{_texdir}/texmf-dist/fonts/type1/public/cyklop/
%{_texdir}/texmf-dist/tex/latex/cyklop/

%files -n texlive-cyklop-doc
%license gfl.txt
%{_texdir}/texmf-dist/doc/fonts/cyklop/

%files -n texlive-dancers
%{_texdir}/texmf-dist/fonts/source/public/dancers/
%{_texdir}/texmf-dist/fonts/tfm/public/dancers/

%files -n texlive-dantelogo
%license lppl1.txt
%{_datadir}/fonts/dantelogo
%{_texdir}/texmf-dist/fonts/enc/dvips/dantelogo/
%{_texdir}/texmf-dist/fonts/map/dvips/dantelogo/
%{_texdir}/texmf-dist/fonts/opentype/public/dantelogo/
%{_texdir}/texmf-dist/fonts/tfm/public/dantelogo/
%{_texdir}/texmf-dist/fonts/type1/public/dantelogo/
%{_texdir}/texmf-dist/fonts/vf/public/dantelogo/
%{_texdir}/texmf-dist/tex/latex/dantelogo/

%files -n texlive-dantelogo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/dantelogo/

%files -n texlive-dejavu
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/dejavu/
%{_texdir}/texmf-dist/fonts/enc/dvips/dejavu/
%{_texdir}/texmf-dist/fonts/map/dvips/dejavu/
%{_texdir}/texmf-dist/fonts/tfm/public/dejavu/
%{_texdir}/texmf-dist/fonts/truetype/public/dejavu/
%{_texdir}/texmf-dist/fonts/type1/public/dejavu/
%{_texdir}/texmf-dist/fonts/vf/public/dejavu/
%{_texdir}/texmf-dist/tex/latex/dejavu/

%files -n texlive-dejavu-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/dejavu/

%files -n texlive-crossword
%{_texdir}/texmf-dist/tex/latex/crossword/

%files -n texlive-crossword-doc
%{_texdir}/texmf-dist/doc/latex/crossword/

%files -n texlive-crosswrd
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/crosswrd/

%files -n texlive-crosswrd-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/crosswrd/

%files -n texlive-c-pascal
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/c-pascal/

%files -n texlive-c-pascal-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/c-pascal/

%files -n texlive-dad
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/dad/
%{_texdir}/texmf-dist/fonts/map/dvips/dad/
%{_texdir}/texmf-dist/fonts/ofm/public/dad/
%{_texdir}/texmf-dist/fonts/ovf/public/dad/
%{_texdir}/texmf-dist/fonts/tfm/public/dad/
%{_texdir}/texmf-dist/fonts/type1/public/dad/
%{_texdir}/texmf-dist/tex/lualatex/dad/

%files -n texlive-dad-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/dad/

%files -n texlive-ctex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/ctex/
%{_texdir}/texmf-dist/tex/latex/ctex/

%files -n texlive-ctex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ctex/

%files -n texlive-ctex-faq-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/latex/ctex-faq/


%files -n texlive-cyrplain
%{_texdir}/texmf-dist/tex/plain/cyrplain/

%files -n texlive-cs
%license gpl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/cs/
%{_texdir}/texmf-dist/fonts/map/dvips/cs/
%{_texdir}/texmf-dist/fonts/source/public/cs/
%{_texdir}/texmf-dist/fonts/tfm/cs/
%{_texdir}/texmf-dist/fonts/tfm/public/cs/
%{_texdir}/texmf-dist/fonts/type1/public/cs/
%{_texdir}/texmf-dist/fonts/vf/cs/

%files -n texlive-csbulletin
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/csbulletin/

%files -n texlive-csbulletin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/csbulletin/

%files -n texlive-cstex-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/cstex/

%files -n texlive-csquotes-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/csquotes-de/

%files -n texlive-dehyph-exptl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/dehyph-exptl/

%files -n texlive-dehyph-exptl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/dehyph-exptl/

%files -n texlive-ctib
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/ctib/
%{_texdir}/texmf-dist/fonts/tfm/public/ctib/
%{_texdir}/texmf-dist/tex/latex/ctib/

%files -n texlive-ctib-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/ctib/

%files -n texlive-cursolatex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/cursolatex/

%files -n texlive-crop
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/crop/

%files -n texlive-crop-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/crop/

%files -n texlive-ctable
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ctable/

%files -n texlive-ctable-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ctable/

%files -n texlive-curve
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/curve/

%files -n texlive-curve-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/curve/

%files -n texlive-curve2e
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/curve2e/

%files -n texlive-curve2e-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/curve2e/

%files -n texlive-curves
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/curves/

%files -n texlive-curves-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/curves/

%files -n texlive-dcpic
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/dcpic/

%files -n texlive-dcpic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/dcpic/

%files -n texlive-cprotect
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cprotect/

%files -n texlive-cprotect-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cprotect/

%files -n texlive-crbox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/crbox/

%files -n texlive-crbox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/crbox/

%files -n texlive-crossreference
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/crossreference/

%files -n texlive-crossreference-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/crossreference/

%files -n texlive-csquotes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/csquotes/

%files -n texlive-csquotes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/csquotes/

%files -n texlive-csvsimple
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/csvsimple/

%files -n texlive-csvsimple-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/csvsimple/

%files -n texlive-cuisine
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cuisine/

%files -n texlive-cuisine-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cuisine/

%files -n texlive-currfile
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/currfile/

%files -n texlive-currfile-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/currfile/

%files -n texlive-currvita
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/currvita/

%files -n texlive-currvita-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/currvita/

%files -n texlive-cutwin
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cutwin/

%files -n texlive-cutwin-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cutwin/

%files -n texlive-cv
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/cv/

%files -n texlive-cv-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/cv/

%files -n texlive-cv4tw
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/cv4tw/

%files -n texlive-cv4tw-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/cv4tw/

%files -n texlive-cweb-latex
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/cweb-latex/

%files -n texlive-cweb-latex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/cweb-latex/

%files -n texlive-cyber
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/cyber/

%files -n texlive-cyber-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/cyber/

%files -n texlive-cybercic
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/cybercic/

%files -n texlive-cybercic-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/cybercic/

%files -n texlive-dashbox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dashbox/

%files -n texlive-dashbox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dashbox/

%files -n texlive-dashrule
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dashrule/

%files -n texlive-dashrule-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dashrule/

%files -n texlive-dashundergaps
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dashundergaps/

%files -n texlive-dashundergaps-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dashundergaps/

%files -n texlive-dataref
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/dataref/

%files -n texlive-dataref-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/dataref/

%files -n texlive-datatool
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/datatool/
%{_texdir}/texmf-dist/tex/latex/datatool/

%files -n texlive-datatool-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datatool/

%files -n texlive-dateiliste
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dateiliste/

%files -n texlive-dateiliste-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dateiliste/

%files -n texlive-datenumber
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/datenumber/

%files -n texlive-datenumber-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/datenumber/

%files -n texlive-datetime
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime/

%files -n texlive-datetime-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime/

%files -n texlive-datetime2
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2/

%files -n texlive-datetime2-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2/

%files -n texlive-datetime2-bahasai
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-bahasai/

%files -n texlive-datetime2-bahasai-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-bahasai/

%files -n texlive-datetime2-basque
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-basque/

%files -n texlive-datetime2-basque-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-basque/

%files -n texlive-datetime2-breton
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-breton/

%files -n texlive-datetime2-breton-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-breton/

%files -n texlive-datetime2-bulgarian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-bulgarian/

%files -n texlive-datetime2-bulgarian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-bulgarian/

%files -n texlive-datetime2-catalan
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-catalan/

%files -n texlive-datetime2-catalan-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-catalan/

%files -n texlive-datetime2-croatian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-croatian/

%files -n texlive-datetime2-croatian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-croatian/

%files -n texlive-datetime2-czech
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-czech/

%files -n texlive-datetime2-czech-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-czech/

%files -n texlive-datetime2-danish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-danish/

%files -n texlive-datetime2-danish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-danish/

%files -n texlive-datetime2-dutch
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-dutch/

%files -n texlive-datetime2-dutch-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-dutch/

%files -n texlive-datetime2-en-fulltext
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-en-fulltext/

%files -n texlive-datetime2-en-fulltext-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-en-fulltext/

%files -n texlive-datetime2-english
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-english/

%files -n texlive-datetime2-english-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-english/

%files -n texlive-datetime2-esperanto
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-esperanto/

%files -n texlive-datetime2-esperanto-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-esperanto/

%files -n texlive-datetime2-estonian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-estonian/

%files -n texlive-datetime2-estonian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-estonian/

%files -n texlive-datetime2-finnish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-finnish/

%files -n texlive-datetime2-finnish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-finnish/

%files -n texlive-datetime2-french
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-french/

%files -n texlive-datetime2-french-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-french/

%files -n texlive-datetime2-galician
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-galician/

%files -n texlive-datetime2-galician-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-galician/

%files -n texlive-datetime2-german
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-german/

%files -n texlive-datetime2-german-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-german/

%files -n texlive-datetime2-greek
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-greek/

%files -n texlive-datetime2-greek-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-greek/

%files -n texlive-datetime2-hebrew
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-hebrew/

%files -n texlive-datetime2-hebrew-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-hebrew/

%files -n texlive-datetime2-icelandic
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-icelandic/

%files -n texlive-datetime2-icelandic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-icelandic/

%files -n texlive-datetime2-irish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-irish/

%files -n texlive-datetime2-irish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-irish/

%files -n texlive-datetime2-italian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-italian/

%files -n texlive-datetime2-italian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-italian/

%files -n texlive-datetime2-it-fulltext
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-it-fulltext/

%files -n texlive-datetime2-it-fulltext-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-it-fulltext/

%files -n texlive-datetime2-latin
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-latin/

%files -n texlive-datetime2-latin-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-latin/

%files -n texlive-datetime2-lsorbian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-lsorbian/

%files -n texlive-datetime2-lsorbian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-lsorbian/

%files -n texlive-datetime2-magyar
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-magyar/

%files -n texlive-datetime2-magyar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-magyar/

%files -n texlive-datetime2-norsk
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-norsk/

%files -n texlive-datetime2-norsk-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-norsk/

%files -n texlive-datetime2-polish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-polish/

%files -n texlive-datetime2-polish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-polish/

%files -n texlive-datetime2-portuges
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-portuges/

%files -n texlive-datetime2-portuges-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-portuges/

%files -n texlive-datetime2-romanian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-romanian/

%files -n texlive-datetime2-romanian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-romanian/

%files -n texlive-datetime2-russian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-russian/

%files -n texlive-datetime2-russian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-russian/

%files -n texlive-datetime2-samin
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-samin/

%files -n texlive-datetime2-samin-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-samin/

%files -n texlive-datetime2-scottish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-scottish/

%files -n texlive-datetime2-scottish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-scottish/

%files -n texlive-datetime2-serbian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-serbian/

%files -n texlive-datetime2-serbian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-serbian/

%files -n texlive-datetime2-slovak
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-slovak/

%files -n texlive-datetime2-slovak-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-slovak/

%files -n texlive-datetime2-slovene
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-slovene/

%files -n texlive-datetime2-slovene-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-slovene/

%files -n texlive-datetime2-spanish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-spanish/

%files -n texlive-datetime2-spanish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-spanish/

%files -n texlive-datetime2-swedish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-swedish/

%files -n texlive-datetime2-swedish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-swedish/

%files -n texlive-datetime2-turkish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-turkish/

%files -n texlive-datetime2-turkish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-turkish/

%files -n texlive-datetime2-ukrainian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-ukrainian/

%files -n texlive-datetime2-ukrainian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-ukrainian/

%files -n texlive-datetime2-usorbian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-usorbian/

%files -n texlive-datetime2-usorbian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-usorbian/

%files -n texlive-datetime2-welsh
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/datetime2-welsh/

%files -n texlive-datetime2-welsh-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/datetime2-welsh/

%files -n texlive-dblfloatfix
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/dblfloatfix/

%files -n texlive-dblfloatfix-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/dblfloatfix/

%files -n texlive-decimal
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/decimal/

%files -n texlive-decimal-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/decimal/

%files -n texlive-decorule
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/decorule/

%files -n texlive-decorule-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/decorule/

%files -n texlive-delim
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/delim/

%files -n texlive-delim-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/delim/

%files -n texlive-delimtxt
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/delimtxt/

%files -n texlive-delimtxt-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/delimtxt/

%files -n texlive-denisbdoc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/denisbdoc/

%files -n texlive-denisbdoc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/denisbdoc/


%files -n texlive-dccpaper
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/dccpaper/

%files -n texlive-dccpaper-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/dccpaper/

%files -n texlive-cryptocode
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cryptocode/

%files -n texlive-cryptocode-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cryptocode/

%files -n texlive-cquthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cquthesis/

%files -n texlive-cquthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cquthesis/
%{_texdir}/texmf-dist/bibtex/bst/cquthesis/

%files -n texlive-crimson-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/crimson/

%files -n texlive-crimson
%license ofl.txt
%{_texdir}/texmf-dist/tex/latex/crimson/
%{_texdir}/texmf-dist/fonts/opentype/kosch/crimson/
%{_texdir}/texmf-dist/fonts/map/dvips/crimson/
%{_texdir}/texmf-dist/fonts/tfm/kosch/crimson/
%{_texdir}/texmf-dist/fonts/vf/kosch/crimson/
%{_texdir}/texmf-dist/fonts/enc/dvips/crimson/
%{_texdir}/texmf-dist/fonts/type1/kosch/crimson/

%files -n texlive-ctablestack-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/luatex/ctablestack/

%files -n texlive-ctablestack
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/luatex/ctablestack/

%files -n texlive-delimseasy-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/delimseasy/

%files -n texlive-delimseasy
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/delimseasy/

%files -n texlive-crossreftools
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/crossreftools/
%{_texdir}/texmf-dist/tex/latex/crossreftools/

%files -n texlive-css-colors
%license lppl.txt gpl.txt
%doc %{_texdir}/texmf-dist/doc/latex/css-colors/
%{_texdir}/texmf-dist/tex/latex/css-colors/

%files -n texlive-cstypo
%doc %{_texdir}/texmf-dist/doc/lualatex/cstypo/
%{_texdir}/texmf-dist/tex/lualatex/cstypo/
%{_texdir}/texmf-dist/tex/luatex/cstypo/

%files -n texlive-currency
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/currency/
%{_texdir}/texmf-dist/tex/latex/currency/

%files -n texlive-cqubeamer
%{_texdir}/texmf-dist/tex/xelatex/cqubeamer/
%doc %{_texdir}/texmf-dist/doc/xelatex/cqubeamer/

%files -n texlive-dejavu-otf
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/dejavu-otf/
%doc %{_texdir}/texmf-dist/doc/fonts/dejavu-otf/

%files -n texlive-delimset
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/delimset/
%doc %{_texdir}/texmf-dist/doc/latex/delimset/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
