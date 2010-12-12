Migrating from APScheduler v1.x to 2.0
======================================

There have been some API changes since the 1.x series. This document
explains the changes made to v2.0 that are incompatible with the v1.x API.

API changes
-----------

* SchedulerShutdownError has been removed -- jobs are now added tentatively
  and scheduled for real when/if the scheduler is restarted
* Scheduler.is_job_active() has been removed -- use
  ``job in scheduler.get_jobs()`` instead
* dump_jobs() is now print_jobs() and prints directly to the given file or
  sys.stdout if none is given
* The ``repeat`` parameter was removed from
  :meth:`apscheduler.scheduler.Scheduler.add_interval_job` and
  :meth:`apscheduler.scheduler.Scheduler.interval_schedule` in favor of the
  universal ``max_runs`` option

Configuration changes
---------------------

* The scheduler can no longer be reconfigured while it's running